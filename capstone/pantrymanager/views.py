from .models import Pantry
from .serializers import PantrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class PantryList(APIView):
    def get (self, request):
        pantry = Pantry.objects.all()
        serializer = PantrySerializer(pantry, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PantrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)