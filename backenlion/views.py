from rest_framework import viewsets
from .models import Food
from .serializers import Fooderializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = Fooderializer