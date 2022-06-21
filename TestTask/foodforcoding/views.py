from foodforcoding.models import Food
from foodforcoding.models import FoodCategory

from rest_framework import permissions
from rest_framework import viewsets
from foodforcoding.serializer import FoodListSerializer
from foodforcoding.serializer import FoodSerializer
from django.db.models import Prefetch

class FoodCategory_view(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
    permission_control = [permissions.AllowAny]

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(Prefetch("food", queryset=Food.objects.filter(is_publish=True)))
        return queryset

class Food_view(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_control = [permissions.AllowAny]