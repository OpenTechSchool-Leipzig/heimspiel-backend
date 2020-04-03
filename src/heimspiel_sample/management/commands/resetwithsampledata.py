import csv
import os

from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File as DjangoFile
from django.db import transaction
from filer.models import File as FilerFile
from filer.models import Image as FilerImage

from heimspiel_core.models import Badge, QuestCategory, PlayerAttribute, Quest


class Command(BaseCommand):
    @transaction.atomic
    def _create_sample_data(self):
        self._create_sample_user()

        categories = {
            "activity": "Beschäftigung",
            "chores": "Hausarbeit",
            "health": "Gesundheit",
            "living-together": "Zusammenleben",
            "productivity": "Produktivität",
            "solidarity": "Zusammenhalt",
        }
        for cat_id, cat_name in categories.items():
            self._create_badge(cat_name, f"{cat_id}.svg")
            categories[cat_id] = self._create_quest_category(
                cat_id, cat_name, f"{cat_id}.jpg"
            )

        attributes = ["Sportskanone", "Witzbold", "Ruhepol", "Sternekoch"]
        for attribute in attributes:
            PlayerAttribute.objects.create(name=attribute)

        self._import_quests_from_csv(categories)

    def _create_sample_user(self):
        self._user = self.User.objects.create(username="sample")

    def _create_badge(self, name, svg_name):
        file_ = self._create_filer_file(f"badges/{svg_name}", svg_name)
        Badge.objects.create(name=name, image=file_)

    def _create_quest_category(self, id_, title, jpg_name):
        file_ = self._create_filer_image(f"questcategories/{jpg_name}", jpg_name)
        QuestCategory.objects.create(id=id_, title=title, image=file_)

    def _import_quests_from_csv(self, categories):
        with open(self._app_path("quests.csv")) as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)  # skip first line
            for row in reader:
                self._create_quest(*row)

    def _create_quest(self, title, category_id, text, flavor_text, score, image):
        file_ = self._create_filer_image(self._app_path(f"quests/{image}"), image)
        Quest.objects.create(
            title=title,
            category_id=category_id,
            text=text,
            flavor_text=flavor_text,
            score=int(score),
            image=file_,
        )

    def _create_filer_file(self, path, name):
        file_obj = DjangoFile(open(self._app_path(path), "r"), name=name)
        return FilerFile.objects.create(
            owner=self._user, file=file_obj, original_filename=name
        )

    def _create_filer_image(self, path, name):
        file_obj = DjangoFile(open(self._app_path(path), "rb"), name=name)
        return FilerImage.objects.create(
            owner=self._user, file=file_obj, original_filename=name
        )

    def _app_path(self, path):
        return os.path.join(self.app_config.path, path)

    def handle(self, *args, **kwargs):
        self._delete_objects()
        self.stdout.write(self.style.SUCCESS("Successfully reset database."))
        self._create_sample_data()
        self.stdout.write(self.style.SUCCESS("Successfully created sample data."))

    def _delete_objects(self):
        FilerImage.objects.all().delete()
        FilerFile.objects.all().delete()

        for app in ["heimspiel_core"]:
            for model in apps.get_app_config(app).get_models():
                model.objects.all().delete()

        self.User.objects.filter(is_superuser=False).delete()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.User = get_user_model()
        self.app_config = apps.get_app_config("heimspiel_sample")
