from rest_framework import serializers
from .models import Massage


class SerializerHellow(serializers.Serializer):
    class Meta:
        model = Massage
        fields = ['massage']
