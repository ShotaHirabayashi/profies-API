from rest_framework.views import APIView
from rest_framework.response import Response




class HelloApiView(APIView):
    """ Test API View"""

    def get(self,request,format=None):
        """Return a lost of  APIView features"""
        an_apiview = [
            "Uses HTTP methids as function(get,post,patch,put,delete)",
            "Is similar to a traditinal Django View",
            "Gives you the most control over you aplicetion logic",
            "Is mapped manually to URLs"
        ]


        return Response({"message":"Hello","an_apiview":an_apiview})