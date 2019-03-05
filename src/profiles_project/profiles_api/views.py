from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers, models, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly     #default django permissions class gives permission to the authendicated user to update their status else readonly
from rest_framework.permissions import IsAuthenticated

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

    serializer_class = serializers.UserProfileSerializer   #validates user profile
    queryset = models.UserProfile.objects.all()            #query and returns list all items from db to frontend(ViewSet get method)
    authentication_classes = (TokenAuthentication,)        #token auth
    permission_classes = (permissions.UpdateOwnProfile,)   #setting permissions for modifying user profiles using ids
    filter_backends = (filters.SearchFilter,)              # search and filter users based on name and email fields
    search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)            #passing the request to ObtainAuthToken

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)#OrReadOnly) #only logged in users can post or update status

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)    #creates user feed(text data input) and associates with currently logged in user
