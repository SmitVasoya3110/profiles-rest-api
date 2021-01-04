from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


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
        print(an_apiview)
        return Response({'message': 'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello,{name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
