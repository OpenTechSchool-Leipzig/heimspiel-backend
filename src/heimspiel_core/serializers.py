from rest_framework import serializers

from .models import Player, PlayerAttribute, Quest, QuestCategory


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
