from rest_framework import serializers
from .models import Food

class Fooderializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'price']