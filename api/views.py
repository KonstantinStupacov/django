from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SerializerMassage, SerializerMaster, SerializerClient, SerializerCategories
from .models import Massage, People, Categories


class MassageView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            massage = Massage.objects.get(pk=pk)
            serializer = SerializerMassage(massage)
            return Response(serializer.data)
        else:
            massage = Massage.objects.all()
            serializer = SerializerMassage(massage, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SerializerMassage(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is not None:
            massage = Massage.objects.get(pk=pk)
            serializer = SerializerMassage(massage, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            massage = Massage.objects.get(pk=pk)
            massage.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            massage = Massage.objects.all()
            massage.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriesView(APIView):
    def get(self, request, uuid=None):  # Add 'pk=None' to the get method
        if uuid is not None:
            categories = Categories.objects.get(uuid=uuid)
            serializer = SerializerCategories(categories)
            return Response(serializer.data)
        else:
            categories = Categories.objects.all()
            serializer = SerializerCategories(categories, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SerializerCategories(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            categories = Categories.objects.get(pk=pk)
            serializer = SerializerCategories(categories, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            categories = Categories.objects.get(pk=pk)
            categories.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            categories = Categories.objects.all()
            categories.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class PeopleView(APIView):
    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            people = People.objects.get(pk=pk)
            serializer = SerializerClient(people)
            return Response(serializer.data)
        else:
            people = People.objects.all()
            serializer = SerializerClient(people, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SerializerClient(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            people = People.objects.get(pk=pk)
            serializer = SerializerClient(people, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            people = People.objects.get(pk=pk)
            people.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            people = People.objects.all()
            people.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
