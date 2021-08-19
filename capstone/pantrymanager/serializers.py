from rest_framework import serializers
from .models import Pantry


class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ['id', 'name', 'type', 'quantity', 'unit', 'expiration']
