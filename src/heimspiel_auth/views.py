from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        response = super().create(request)
        token = Token.objects.get(user_id=response.data["id"])
        response.data["token"] = token.key
        return response
