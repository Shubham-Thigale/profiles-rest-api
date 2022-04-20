from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):   #self is the parameter which is required by all class function, a request object is passed by django rest framework and contains details of request made to API, format is used to add format suffix to endpoint URL which we are not using in this case
        """Returns a list of APIView features"""
        an_apiview = [
        'Name-Shubham',
        'Org-HSPL',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
