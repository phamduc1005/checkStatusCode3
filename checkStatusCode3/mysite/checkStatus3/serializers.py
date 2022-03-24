from rest_framework import serializers
from .models import CheckUrl, UrlError




class UrlErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlError
        fields = ('status', 'url', 'checkUrl')

class CheckUrlSerializer(serializers.ModelSerializer):
    error = UrlErrorSerializer(many=True, read_only = True)
    class Meta:
        model = CheckUrl
        fields = ('id', 'test', 'time', 'error')
