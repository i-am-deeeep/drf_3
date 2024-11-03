from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import register_view, logout_view

urlpatterns = [
    path("login/", obtain_auth_token),
    path("register/", register_view),
    path("logout/", logout_view),
]