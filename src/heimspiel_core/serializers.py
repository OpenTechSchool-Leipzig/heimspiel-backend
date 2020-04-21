from rest_framework import serializers

from .models import Badge, Player, PlayerAttribute, Quest, QuestCategory


class GetImageMixin:
    def get_image(self, obj):
        if obj.image is not None:
            request = self.context["request"]
            return request.build_absolute_uri(obj.image.url)
        else:
            return None


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Player
        fields = ["id", "user", "name", "score", "background_story", "attributes"]


class PlayerAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAttribute
        fields = ["id", "name"]


class QuestSerializer(serializers.ModelSerializer, GetImageMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Quest
        fields = ["id", "title", "category", "text", "flavor_text", "score", "image"]


class QuestCategorySerializer(serializers.ModelSerializer, GetImageMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = QuestCategory
        fields = ["id", "title", "image"]


class BadgeSerializer(serializers.ModelSerializer, GetImageMixin):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Badge
        fields = ["id", "name", "image"]
