from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from . import views

app_name = "api"

urlpatterns = [
    path("", views.simple_view, name="api_simple_view"),
    path("question/", views.question_view, name="api_question_view"),
    path("question/create/", views.question_create_view, name="api_question_create_view"),
    path("authenticate/", views.ProtectedView.as_view(), name="api_protected_view"),
]
