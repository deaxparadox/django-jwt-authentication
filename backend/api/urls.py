from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from . import views

app_name = "api"

urlpatterns = [
    path("", views.simple_view, name="api_simple_view"),
]
