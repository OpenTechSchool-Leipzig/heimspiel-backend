from rest_framework import serializers

from .models import Player, PlayerAttribute, Quest, QuestCategory


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'user', 'name', 'score', 'background_story',
                  'attributes']


class PlayerAttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerAttribute
        fields = ['url', 'name']


class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quest
        fields = ['url', 'title', 'category', 'text', 'flavor_text', 'score']


class QuestCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestCategory
        fields = ['url', 'title']


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestCategory
        fields = ['url', 'name']
