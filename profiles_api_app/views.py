from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated




from profiles_api_app import serializers
from profiles_api_app import models
from profiles_api_app import permissions


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
    def put(self,request,pk=None):
        """hndle put request"""
        return Response({'message':'server recieve a put request'})
    
    def patch(self,request,pk=None):
        """hndle patch request"""
        return Response({'message':'server recieve a patch request'})
    
    def delete(self,request,pk=None):
        """hndle delete request"""
        return Response({'message':'server recieve a delete request'})
    
class Testapiviewsets(viewsets.ViewSet):
    """a class to test aapiviewSets """

    serializer_class = serializers.testApiSerializer


    def list(self,request):
        """handl list of all objects"""
        randomData = ['res 1','res 2','res 3']
        return Response({'message':'success','data':randomData})
    
    def create(self,request):
        """handle creating aan object"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message':f'hello dear {name}'})
        else:
            return Response(serializer.errors,status=400)
    def retrieve(self,request,pk=None):
        """hndle getting one  object"""
        return Response({'message':'server recieve a get one object request'})
    def update(self,request,pk=None):
        """hndle updateing an object"""
        return Response({'message':'server recieve a update object request'})
    def partial_update(self,request,pk=None):
        """hndle partial update of object"""
        return Response({'message':'server recieve a partial_update object request'})
    
    def destroy(self,request,pk=None):
        """hndle destroy object"""
        return Response({'message':'server recieve a destroy object request'})


class UserProfilViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.userProfilSerilizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfilFeedViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.userFeedSerializer
    queryset = models.ProfileFeed.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated)
    def perform_create(self, serializer):
        """ Sets the user profile to the logged user"""
        serializer.save(user_profile=self.request.user)