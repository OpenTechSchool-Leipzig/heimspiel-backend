from django.db import models


class QuestCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    title = models.CharField(max_length=64)
    # TODO: image


class Quest(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(QuestCategory, on_delete=models.CASCADE)
    text = models.TextField()
    flavor_text = models.TextField()
    score = models.IntegerField()
    # TODO: image
