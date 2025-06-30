from django.urls import path

import users.views
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
TokenVerifyView
)

urlpatterns = [
    path('', views.Users.as_view()),
    path("myinfo/", views.MyInfo.as_view()),

    #Authentication
    path("getToken", obtain_auth_token),  #DRF Token
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),  #DRF Token logout
    #Django Session login

    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetailView.as_view()), #JWT login

    path("login/simplejwt", TokenObtainPairView.as_view()),
    path("login/simplejwt/refresh", TokenRefreshView.as_view()),
    path("login/simplejwt/verify", TokenVerifyView.as_view()),
]