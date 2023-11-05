from rest_framework import serializers


class testApiSerializer(serializers.Serializer):
    """serializers for testapi request data fields (name)"""
    name = serializers.CharField(max_length=10)