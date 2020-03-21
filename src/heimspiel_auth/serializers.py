import uuid

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['id', 'name']

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data['username'] = validated_data['id']
        validated_data['password'] = ''
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return user
