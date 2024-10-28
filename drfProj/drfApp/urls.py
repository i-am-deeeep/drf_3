from django.urls import path, include
from drfApp import views

urlpatterns = [
    path("bloglist/", views.BlogListCV.as_view()),
    path("blog/<int:pk>/", views.BlogDetailCV.as_view()),
]