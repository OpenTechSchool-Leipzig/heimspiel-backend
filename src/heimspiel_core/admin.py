from django.contrib import admin

from .models import Badge, Player, PlayerAttribute, Quest, QuestCategory, ScoreReport

admin.site.register(PlayerAttribute)
admin.site.register(Player)
admin.site.register(Quest)
admin.site.register(QuestCategory)
admin.site.register(ScoreReport)
admin.site.register(Badge)
