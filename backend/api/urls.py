from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from . import views

app_name = "api"

urlpatterns = [
    path("", views.simple_view, name="api_simple_view"),
    

    # fetch question
    # query parameters
    # all=True: fetch all question
    # id=<int>: fetch question of specified id
    path("question/", views.QuestionView.as_view(), name="api_question_view"),

    # create question
    path("question/create/", views.question_create_view, name="api_question_create_view"),
    
    # authenticated user view
    path("authenticate/", views.ProtectedView.as_view(), name="api_protected_view"),
]
