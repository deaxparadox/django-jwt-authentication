from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(["GET", "POST"])
def simple_view(request):
    if request.method == "POST":
        print(request.data)
        return Response({"message": "Recieved a POST Request"}, status=status.HTTP_202_ACCEPTED)    

    return Response({"message": "Hello Everyone"}, status=status.HTTP_200_OK)


class ProtectedView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        ...