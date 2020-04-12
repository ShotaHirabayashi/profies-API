from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers




class HelloApiView(APIView):
    """ Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a lost of  APIView features"""
        an_apiview = [
            "Uses HTTP methids as function(get,post,patch,put,delete)",
            "Is similar to a traditinal Django View",
            "Gives you the most control over you aplicetion logic",
            "Is mapped manually to URLs"
        ]


        return Response({"message":"Hello","an_apiview":an_apiview})


    def post(self,request):
        """create a hello msg with our name"""
        serializer  = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print("hi")
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )



    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({"method":'PUT'})

    def patch(self,request,pk=None):
        """Handle partial update an object"""
        return Response({"method":'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({"method":'DELETE'})


class HelloApiViewSet(viewsets.ViewSet):
    """Test API viewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):

        a_viewset =[
            'Uses actions (list create ,retrive)',
            "Automatiaclly maps to URLs using Routers",
            "Provides more functinality with less code"
        ]

        return Response({"message":"Hello","a_viewser":a_viewset})


    def create(self,request):
        """create a new hello message"""
        serializer = selfserializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrive(self,request,pk=None):
        """Handle getting an object by itsID"""
        return Response({"http:method":"GET"})

    def update(self,request,pk=None):
        """Handle updateting an object by itsID"""
        return Response({"http:method":"UPDATE"})

    def partial_update(self,request,pk=None):
        """Handle updateting an object"""
        return Response({"http:method":"PATCH"})


    def destroy(self,request,pk=None):
        """Handle removing an objec"""
        return Response({"http:method":"DELETE"})