from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

from heimspiel_auth.models import User


class PlayerAttribute(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    score = models.PositiveIntegerField(default=0)
    background_story = models.TextField(blank=True)
    attributes = models.ManyToManyField(PlayerAttribute, blank=True)
    # TODO: badges

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class QuestCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    title = models.CharField(max_length=64)
    image = FilerImageField(on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


class Quest(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(QuestCategory, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    flavor_text = models.TextField(blank=True)
    score = models.IntegerField()
    image = FilerImageField(
        null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


class ScoreReport(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        QuestCategory, through="QuestCategoryScoreReport"
    )

    def __str__(self):
        return f"Report of {self.player} ({self.date})"

    class Meta:
        ordering = ["date", "id"]


class QuestCategoryScoreReport(models.Model):
    category = models.ForeignKey(QuestCategory, on_delete=models.CASCADE)
    report = models.ForeignKey(ScoreReport, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()


class Badge(models.Model):
    name = models.CharField(max_length=64)
    # FilerFileField instead of FilerImageField because we want to use SVGs
    image = FilerFileField(on_delete=models.CASCADE)
    # TODO: constraints

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
