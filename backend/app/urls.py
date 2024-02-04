from django.urls import path, re_path, include

from . import views

app_name = "app"

urlpatterns = [
    path("", views.simple_view, name="app_simple_view")
]
