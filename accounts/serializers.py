from dataclasses import fields
from pyexpat import model
from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model

User = get_user_model

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'name', 'password']