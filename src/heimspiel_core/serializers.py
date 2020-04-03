from rest_framework import serializers

from .models import Badge, Player, PlayerAttribute, Quest, QuestCategory


class GetImageMixin:
    def get_image(self, obj):
        if obj.image is not None:
            request = self.context["request"]
            return request.build_absolute_uri(obj.image.url)
        else:
            return None


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Player
        fields = ["url", "user", "name", "score", "background_story", "attributes"]


class PlayerAttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerAttribute
        fields = ["url", "name"]


class QuestSerializer(serializers.HyperlinkedModelSerializer, GetImageMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Quest
        fields = ["url", "title", "category", "text", "flavor_text", "score", "image"]


class QuestCategorySerializer(serializers.HyperlinkedModelSerializer, GetImageMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = QuestCategory
        fields = ["url", "title", "image"]


class BadgeSerializer(serializers.HyperlinkedModelSerializer, GetImageMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Badge
        fields = ["url", "name", "image"]
