from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SerializerHellow
from .models import Massage


class SayHellow(APIView):
    def get(self, request):
        queryset = Massage.objects.all()
        serializer = SerializerHellow(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)
