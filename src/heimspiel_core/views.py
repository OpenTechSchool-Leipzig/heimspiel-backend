from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import (
    Player,
    PlayerAttribute,
    Quest,
    QuestCategory,
    Badge,
    ScoreReport,
    QuestCategoryScoreReport,
)
from .score import UserScoreReportSerializer, ScoreReportResponseSerializer
from .serializers import (
    PlayerSerializer,
    PlayerAttributeSerializer,
    QuestSerializer,
    QuestCategorySerializer,
    BadgeSerializer,
)


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlayerAttributeSerializer
    queryset = PlayerAttribute.objects.all()
    permission_classes = [permissions.AllowAny]


class QuestViewSet(viewsets.ModelViewSet):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class QuestCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestCategorySerializer
    queryset = QuestCategory.objects.all()
    permission_classes = [permissions.AllowAny]


class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
    permission_classes = [permissions.AllowAny]


<<<<<<< a08e5f79b7975dc1a403dcec22c359d6d479f0a3
@api_view(["POST"])
=======
score_reports_response = openapi.Response("", ScoreReportResponseSerializer)

@swagger_auto_schema(method="post", request_body=UserScoreReportSerializer, responses={201: score_reports_response})
@api_view(["POST"])
>>>>>>> Add score_reports to API docs
def score_reports(request):
    report = UserScoreReportSerializer(data=request.data, context={"request": request})
    report.is_valid(raise_exception=True)
    report = report.validated_data

    user_score = 0
    player_scores = []

    for r in report["report"]:
        player = r["player"]
        sr = ScoreReport.objects.create(player=player, date=report["date"])
        for c in r["category_scores"]:
            QuestCategoryScoreReport.objects.create(
                category=c["category"], report=sr, score=c["score"]
            )
            player.score += c["score"]
        player.save()
        player_scores.append(
            {
                "player": reverse("player-detail", args=[player], request=request),
                "score": player.score,
            }
        )
        user_score += player.score

    return Response(
        {
            "new_scores": {"user": user_score, "players": player_scores,},
            "earned_badges": {"user": [], "players": [],},
        },
        status=201,
    )
