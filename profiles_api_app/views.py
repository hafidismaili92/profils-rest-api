from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api_app import serializers


class TestApiView(APIView):
    """a class to test aapiviews """

    serializer_class = serializers.testApiSerializer

    def get(self,request,format=None):
        randomData = ['res 1','res 2','res 3']
        return Response({'message':'success','data':randomData})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message':f'hello dear {name}'})
        else:
            return Response(serializer.errors,status=400)
    def put(self,reuest,pk=None):
        """hndle put request"""
        return Response({'message':'server recieve a put request'})
    def patch(self,reuest,pk=None):
        """hndle patch request"""
        return Response({'message':'server recieve a patch request'})
    def delete(self,reuest,pk=None):
        """hndle delete request"""
        return Response({'message':'server recieve a delete request'})