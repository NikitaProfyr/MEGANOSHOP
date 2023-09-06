from django.urls import path

from userapp.api import signIn, signUp, signOut, ProfileApi, ProfileResetPasswordApi


app_name = 'user_app'


urlpatterns = [
    path("sign-in", signIn.as_view(), name="Login"),
    path("sign-up", signUp.as_view(), name="Register"),
    path("sign-out", signOut, name="LogOut"),
    path("profile", ProfileApi.as_view(), name="Profile"),
    path(
        "profile/password", ProfileResetPasswordApi.as_view(), name="ProfilePassword"
    ),
]