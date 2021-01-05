from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import permissions
from .models import UserProfile


# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""

        an_apiview = [
            'Uses HHTP method as function(get, post, patch, put, delete)'
            'Is similar to a  traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello,{name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk=None):
    #     """To update existing data"""
    #     return Response({'message': 'Content Updated'})

    def patch(self, request, pk=None):
        """To partially update data"""
        return Response({'message': 'Content Partially Updated'})

    def delete(self, request, pk=None):
        """To delete the data"""
        return Response({'message': 'Content deleted'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a Hello Message"""

        a_viewset = [
            'uses action list, create, retrieve, update, partial_update',
            'Automatically maps URLs using Routers',
            'Provides more funcionalitites with less code'
        ]
        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Handle geting an object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """Updates an objec by its ID"""
        return Response({'Http':'PUT'})

    def partial_update(self, request, pk=None):
        """Updating part of object"""
        return Response({'Http':'Patch'})

    def destroy(self, request, pk=None):
        """Updating part of object"""
        return Response({'Http':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_calsses = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',) 


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication Tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
