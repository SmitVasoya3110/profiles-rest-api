from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

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
