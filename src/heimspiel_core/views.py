from rest_framework import viewsets

from .models import Player, PlayerAttribute, Quest, QuestCategory, Badge
from .serializers import (
    PlayerSerializer, PlayerAttributeSerializer, QuestSerializer,
    QuestCategorySerializer, BadgeSerializer,
)


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerAttributeViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerAttributeSerializer
    queryset = PlayerAttribute.objects.all()


class QuestViewSet(viewsets.ModelViewSet):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()


class QuestCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = QuestCategorySerializer
    queryset = QuestCategory.objects.all()


class BadgeViewSet(viewsets.ModelViewSet):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
