from foodforcoding import views
from rest_framework import routers

v1_router = routers.DefaultRouter()
v1_router.register('foods', views.FoodCategory_view)