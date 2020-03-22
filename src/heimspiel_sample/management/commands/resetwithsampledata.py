import os

from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File as DjangoFile
from django.db import transaction
from filer.models import File as FilerFile
from filer.models import Image as FilerImage

from heimspiel_core.models import Badge, QuestCategory


class Command(BaseCommand):

    @transaction.atomic
    def _create_sample_data(self):
        categories = {
            'activity': 'Beschäftigung',
            'chores': 'Hausarbeit',
            'health': 'Gesundheit',
            'living-together': 'Zusammenleben',
            'productivity': 'Produktivität',
            'solidarity': 'Zusammenhalt',
        }
        for cat_id, cat_name in categories.items():
            self._create_badge(cat_name, f'{cat_id}.svg')
            self._create_quest_category(cat_id, cat_name, f'{cat_id}.jpg')

    def _create_badge(self, name, svg_name):
        file = self._create_filer_file(f'badges/{svg_name}', svg_name)
        Badge.objects.create(name=name, image=file)

    def _create_quest_category(self, id_, title, jpg_name):
        file = self._create_filer_image(f'questcategories/{jpg_name}', jpg_name)
        QuestCategory.objects.create(id=id_, title=title, image=file)

    def _create_filer_file(self, path, name):
        app_path = apps.get_app_config('heimspiel_sample').path
        path = os.path.join(app_path, path)
        user = get_user_model().objects.first()  # TODO: hacky
        file_obj = DjangoFile(open(path, 'r'), name=name)
        return FilerFile.objects.create(
            owner=user, file=file_obj, original_filename=name)

    def _create_filer_image(self, path, name):
        app_path = apps.get_app_config('heimspiel_sample').path
        path = os.path.join(app_path, path)
        user = get_user_model().objects.first()  # TODO: hacky
        file_obj = DjangoFile(open(path, 'rb'), name=name)
        return FilerImage.objects.create(
            owner=user, file=file_obj, original_filename=name)

    def handle(self, *args, **kwargs):
        self._delete_objects()
        self.stdout.write(self.style.SUCCESS(
            'Successfully reset database.'))
        self._create_sample_data()
        self.stdout.write(self.style.SUCCESS(
            'Successfully created sample data.'))

    def _delete_objects(self):
        for app in ['heimspiel_core']:
            for model in apps.get_app_config(app).get_models():
                model.objects.all().delete()


    @staticmethod
    def create_filer_image(user, image_name):
        """
        Create a filer image object suitable for FilerImageField
        It also sets the following attributes:

        * ``self.image_name``: the image base name
        * ``self.filename``: the complete image path
        * ``self.filer_image``: the filer image object

        :param user: image owner
        :param image_name: image name
        :return: filer image object

        It requires Pillow and django-filer installed in the environment to work

        """
        from filer.models import Image

        file_obj, filename = Command.create_django_image()
        filer_image = Image.objects.create(owner=user, file=file_obj, original_filename=image_name)
        return filer_image

    @staticmethod
    def create_django_image():
        """
        Create a django image file object suitable for FileField
        It also sets the following attributes:

        * ``self.image_name``: the image base name
        * ``self.filename``: the complete image path

        :return: (django file object, path to file image)

        It requires Pillow installed in the environment to work
        """
        from django.core.files import File as DjangoFile

        img = Command.create_image()
        image_name = "test_file.jpg"
        if settings.FILE_UPLOAD_TEMP_DIR:
            tmp_dir = settings.FILE_UPLOAD_TEMP_DIR
        else:
            tmp_dir = mkdtemp()
        filename = os.path.join(tmp_dir, image_name)
        img.save(filename, "JPEG")
        return DjangoFile(open(filename, "rb"), name=image_name), filename

    @staticmethod
    def create_image(mode="RGB", size=(800, 600)):
        """
        Create a random image suitable for saving as DjangoFile
        :param mode: color mode
        :param size: tuple of width, height
        :return: image object

        It requires Pillow installed in the environment to work

        """
        from PIL import Image as PilImage, ImageDraw

        image = PilImage.new(mode, size)
        draw = ImageDraw.Draw(image)
        x_bit, y_bit = size[0] // 10, size[1] // 10
        draw.rectangle((x_bit, y_bit * 2, x_bit * 7, y_bit * 3), "red")
        draw.rectangle((x_bit * 2, y_bit, x_bit * 3, y_bit * 8), "red")
        return image
