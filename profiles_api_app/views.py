from rest_framework.views import APIView
from rest_framework.response import Response


class TestApiView(APIView):
    """a class to test aapiviews """
    def get(self,request,format=None):
        randomData = ['res 1','res 2','res 3']
        return Response({'message':'success','data':randomData})