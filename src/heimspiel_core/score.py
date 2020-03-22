import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

from rest_framework import serializers


@dataclass
class CategoryScoreReport:
    category: str
    score: int


@dataclass
class PlayerScoreReport:
    player: str
    category_scores: List[CategoryScoreReport]


@dataclass
class UserScoreReport:
    user: str
    date: datetime
    report: List[PlayerScoreReport]


class CategoryScoreReportSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=255)
    score = serializers.IntegerField()


class PlayerScoreReportSerializer(serializers.Serializer):
    player = serializers.CharField(max_length=255)
    category_scores = CategoryScoreReportSerializer(many=True)


class UserScoreReportSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    report = PlayerScoreReportSerializer(many=True)
