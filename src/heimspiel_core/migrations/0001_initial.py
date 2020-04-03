# Generated by Django 3.0.4 on 2020-03-22 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("filer", "0011_auto_20190418_0137"),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("score", models.PositiveIntegerField(default=0)),
                ("background_story", models.TextField(blank=True)),
            ],
            options={"ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="PlayerAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
            ],
            options={"ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="QuestCategory",
            fields=[
                (
                    "id",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=64)),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["id"],},
        ),
        migrations.CreateModel(
            name="QuestCategoryScoreReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.PositiveIntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="heimspiel_core.QuestCategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ScoreReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        through="heimspiel_core.QuestCategoryScoreReport",
                        to="heimspiel_core.QuestCategory",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="heimspiel_core.Player",
                    ),
                ),
            ],
            options={"ordering": ["date", "id"],},
        ),
        migrations.AddField(
            model_name="questcategoryscorereport",
            name="report",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="heimspiel_core.ScoreReport",
            ),
        ),
        migrations.CreateModel(
            name="Quest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("text", models.TextField(blank=True)),
                ("flavor_text", models.TextField(blank=True)),
                ("score", models.IntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="heimspiel_core.QuestCategory",
                    ),
                ),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.FILER_IMAGE_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["id"],},
        ),
        migrations.AddField(
            model_name="player",
            name="attributes",
            field=models.ManyToManyField(to="heimspiel_core.PlayerAttribute"),
        ),
        migrations.AddField(
            model_name="player",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "image",
                    filer.fields.file.FilerFileField(
                        on_delete=django.db.models.deletion.CASCADE, to="filer.File"
                    ),
                ),
            ],
            options={"ordering": ["id"],},
        ),
    ]
