from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import (
    Player, PlayerAttribute, Quest, QuestCategory, Badge, ScoreReport,
    QuestCategoryScoreReport,
)
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
    report = UserScoreReportSerializer(
        data=request.data, context={'request': request})
    report.is_valid(raise_exception=True)
    report = report.validated_data

    user_score = 0
    player_scores = []

    for r in report['report']:
        player = r['player']
        sr = ScoreReport.objects.create(player=player, date=report['date'])
        for c in r['category_scores']:
            QuestCategoryScoreReport.objects.create(
                category=c['category'], report=sr, score=c['score'])
            player.score += c['score']
        player.save()
        player_scores.append({
            'player': reverse('player-detail', args=[player], request=request),
            'score': player.score,
        })
        user_score += player.score

    return Response({
        'new_scores': {
            'user': user_score,
            'players': player_scores,
        },
        'earned_badges': {
            'user': [],
            'players': [],
        },
    }, status=201)
