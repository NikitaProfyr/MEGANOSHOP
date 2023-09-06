import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from userapp.serializers import ProfileSerializer
from userapp.models import Profile


class signIn(APIView):
    """Класс авторизации на сайте"""

    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(
                status=status.HTTP_201_CREATED
            )  # статусы такие берутся от сюда from rest_framework import status

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class signUp(APIView):
    """Класс регистрации на сайте"""

    def post(self, request):
        user_data = json.loads(self.request.body)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")

        try:
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user, userName=name)
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(request, user)

            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def signOut(request):
    """Функция выхода из личного кабинета"""
    logout(request)
    return HttpResponse(status=200)


class ProfileApi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]  # пишем пермиш потому что сюда не авторизованные заходить не могут

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileResetPasswordApi(APIView):
    """Смена пароля от аккаунта"""

    def post(self, request: HttpRequest):
        data = self.request.data
        userRequest = self.request.user.id
        userModel = User.objects.get(id=userRequest)
        userModel.set_password(data["newPassword"])
        userModel.save()
        return HttpResponse(status=200)
