"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
from rest_framework import serializers
from imageApp.models import images_caption


class imagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = images_caption
        fields = '__all__'
