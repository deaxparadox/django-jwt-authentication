from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.conf import settings

from .serializer import QuestionCreate


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
    return Response({}, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def question_create_view(request):
    serializer = QuestionCreate(data=request.data)
    if serializer.is_valid():
        poll = serializer.create(serializer.validated_data)
        print(poll)
    return Response({}, status=status.HTTP_201_CREATED)