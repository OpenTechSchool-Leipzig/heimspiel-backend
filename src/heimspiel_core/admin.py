from django.contrib import admin

from .models import Badge, Player, PlayerAttribute, Quest, QuestCategory, QuestReport

admin.site.register(PlayerAttribute)
admin.site.register(Player)
admin.site.register(Quest)
admin.site.register(QuestCategory)
admin.site.register(QuestReport)
admin.site.register(Badge)
