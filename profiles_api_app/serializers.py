from rest_framework import serializers

from profiles_api_app import models


class testApiSerializer(serializers.Serializer):
    """serializers for testapi request data fields (name)"""
    name = serializers.CharField(max_length=10)


class userProfilSerilizer(serializers.ModelSerializer):
    """serializer for userProfil object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }


    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name=validated_data['name'],
            password = validated_data['password']
        )

        return user

class userFeedSerializer(serializers.ModelSerializer):
    """serializer for userFeed object"""
    class Meta:
        model = models.ProfileFeed
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {
            'user_profile':{'read_only':True}
        }
    