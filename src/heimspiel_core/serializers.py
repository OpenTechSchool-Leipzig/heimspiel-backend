from rest_framework import serializers

from .models import Badge, Player, PlayerAttribute, Quest, QuestCategory


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
    image = serializers.SerializerMethodField()

    class Meta:
        model = Quest
        fields = ['url', 'title', 'category', 'text', 'flavor_text', 'score',
                  'image']

    def get_image(self, obj):
        if obj.image is not None:
            return obj.image.url
        else:
            return None


class QuestCategorySerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = QuestCategory
        fields = ['url', 'title', 'image']

    def get_image(self, obj):
        if obj.image is not None:
            return obj.image.url
        else:
            return None


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Badge
        fields = ['url', 'name', 'image']

    def get_image(self, obj):
        if obj.image is not None:
            return obj.image.url
        else:
            return None
