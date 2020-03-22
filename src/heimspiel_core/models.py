from django.db import models


class PlayerAttribute(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=64)
    score = models.PositiveIntegerField(default=0)
    background_story = models.TextField(blank=True)
    attributes = models.ManyToManyField(PlayerAttribute)
    # TODO: badges

    def __str__(self):
        return self.name


class QuestCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    title = models.CharField(max_length=64)
    # TODO: image

    def __str__(self):
        return self.title


class Quest(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(QuestCategory, on_delete=models.CASCADE)
    text = models.TextField()
    flavor_text = models.TextField()
    score = models.IntegerField()
    # TODO: image

    def __str__(self):
        return self.title


class QuestReport(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quests = models.ManyToManyField(Quest)

    def __str__(self):
        return f"Report of {self.player} ({self.date})"


class Badge(models.Model):
    name = models.CharField(max_length=64)
    # TODO: constraints

    def __str__(self):
        return self.name
