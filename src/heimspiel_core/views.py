from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Player, PlayerAttribute, Quest, QuestCategory, Badge
from .score import UserScoreReportSerializer
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


@api_view(['POST'])
def score_reports(request):
    report = UserScoreReportSerializer(data=request.data)
    report.is_valid(raise_exception=True)
    return Response({
        'new_scores': {
            'user': 0,
            'players': [
                { 'player': '', 'score': 0, },
                { 'player': '', 'score': 0, },
            ],
        },
        'earned_badges': {
            'user': [],
            'players': [],
        },
    }, status=201)
