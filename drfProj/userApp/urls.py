from django.urls import path
from drfApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, LogoutView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path('register/',RegistrationView.as_view()),
    path('logout/',LogoutView.as_view()),
]