# Generated by Django 3.0.4 on 2020-03-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heimspiel_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='flavor_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
