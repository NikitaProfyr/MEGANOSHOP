from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from userapp.models import Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["userName", "bio"]
