from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of API view features"""

        api=['get','post','put','del']

        return Response({'message':api})
