from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag' , 'id']

class RoomSerializer(serializers.ModelSerializer):
    room_tag = TagSerializer(many =True)
    class Meta:
        model = Room
        fields = '__all__'
        # read_only_fields = ['room_tag']
