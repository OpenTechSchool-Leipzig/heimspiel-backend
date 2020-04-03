import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

from rest_framework import serializers

from heimspiel_auth.models import User
from heimspiel_core.models import Player, QuestCategory


@dataclass
class CategoryScoreReport:
    category: QuestCategory
    score: int


@dataclass
class PlayerScoreReport:
    player: Player
    category_scores: List[CategoryScoreReport]


@dataclass
class UserScoreReport:
    user: User
    date: datetime
    report: List[PlayerScoreReport]


class CategoryScoreReportSerializer(serializers.Serializer):
    category = serializers.HyperlinkedRelatedField(
        queryset=QuestCategory.objects.all(),
        view_name='questcategory-detail')
    score = serializers.IntegerField()


class PlayerScoreReportSerializer(serializers.Serializer):
    player = serializers.HyperlinkedRelatedField(
        queryset=Player.objects.all(),
        view_name='player-detail')
    category_scores = CategoryScoreReportSerializer(many=True)


class UserScoreReportSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date = serializers.DateTimeField()
    report = PlayerScoreReportSerializer(many=True)
