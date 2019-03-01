from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models


# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view features"""

        api=['get','post','put','del']

        return Response({"message" : api})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get("name")
            message = "Hello {0}".format(name)
            return Response({"message" : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({"method": "delete"})

class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'User actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS to routers',
            'provides more functionality with less code'
        ]
        return Response({"message":a_viewset})

    def create(self, request):
        """create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({"message":message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""

        return Response({"http_method":"GET"})

    def update(self, request, pk=None):
        """update an object"""

        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        """partially update an object"""

        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        """deletes an object"""

        return Response({"http_method":"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()            #query and list all items from db
