from django.shortcuts import render, redirect
from django.urls import reverse

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from django.conf import settings

from app.models import Question, Option, Poll
from .serializer import QuestionCreateSerializer, QuestionSerializer


class QuerySetSerialize:
    def query_set_id_serialize(self, question_id):
        query_set = Question.objects.get(id=question_id)
        serializer = QuestionSerializer(query_set)
        return serializer
    
    def query_set_all_serialize(self):
        query_set = Question.objects.all()
        serializer = QuestionSerializer(query_set, many=True)
        return serializer
    

@api_view(["GET", "POST"])
@permission_classes([permissions.AllowAny,])
def simple_view(request):
    # print(request.META)
    if request.method == "POST":
        return Response({"message": "Recieved a POST Request"}, status=status.HTTP_202_ACCEPTED)    

    return Response({"message": "Hello Everyone"}, status=status.HTTP_200_OK)


class ProtectedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None, *args, **kwargs):
        # print(request.META)
        return Response({"message": "Welcome to protected view :)"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def question_view(request):
    question = Question.objects.all()
    serializer: QuestionSerializer = QuestionSerializer(question, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class QuestionView(APIView, QuerySetSerialize):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None, *args, **kwargs):
        all = request.GET.get("all", None)
        question_id = request.GET.get("id", None)

        # if `all` and `question_id` are both absent or both present,
        # redirect to return `all` questions 
        if (not all and not question_id) or (all and question_id):
            return redirect("{}?all=True".format(reverse("api:api_question_view")))
        if all:
            return Response(
                data=self.query_set_all_serialize().data, 
                status=status.HTTP_200_OK
            )
        if isinstance(question_id, (str, int)):
            return Response(
                data=self.query_set_id_serialize(question_id).data, 
                status=status.HTTP_200_OK
                )
        return Response(
            {},
            status=status.HTTP_200_OK
        )
    


class QuestionListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def question_create_view(request):
    serializer = QuestionCreateSerializer(data=request.data)
    if serializer.is_valid():
        poll = serializer.create(serializer.validated_data)
        print(poll)
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)