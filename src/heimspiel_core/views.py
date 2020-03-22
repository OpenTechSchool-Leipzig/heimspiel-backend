from rest_framework import generics

from .models import Player
from .serializers import PlayerSerializer


class GetPlayer(generics.RetrieveAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
