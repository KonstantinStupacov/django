from rest_framework import serializers
from rest_framework.relations import RelatedField

from .models import Massage, People, Categories, Orders


# Изучить типы полей в сериалайзере
class SerializerMassage(serializers.Serializer):
    people = RelatedField(many=True, read_only=True)

    class Meta:
        model = Massage
        fields = ["__all__"]


"""  
  name = serializers.CharField(validators=[])
    name = serializers.SerializerMethodField(method_name='chek_name')
    def chek_name(self, value, *args, **kwargs):
        raise serializers.ValidationError(value)
"""


class SerializerMaster(serializers.Serializer):
    class Meta:
        model = People
        fields = ['__all__']


class SerializerClient(serializers.Serializer):
    class Meta:
        model = People
        fields = ['__all__']


class SerializerCategories(serializers.Serializer):
    massage = RelatedField(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['name']


class SerializerOrder(serializers.Serializer):
    orders = RelatedField(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = ["__all__"]
