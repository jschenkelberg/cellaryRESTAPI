from django.http import Http404

from .models import Food
from .serializers import FoodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PantryList(APIView):
    def get (self, request):
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodDetails(APIView):

    def get_object(self, pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        food = self.get_object(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def put(self, request, pk):
       food = self.get_object(pk)
       serializer = FoodSerializer(food, data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        food = self.get_object(pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        food = self.get_object(pk)
        serializer = FoodSerializer(food, data=request.data, partial=True)
        if serializer.is_valid():
            food.alert = True
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)