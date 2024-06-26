# urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'food', views.FoodViewSet)
router.register(r'food_comment', views.Food_commentViewSet)
router.register(r'restaurant_comment', views.Restaurant_commentViewSet)
router.register(r'restaurant_location', views.Restaurant_locationViewSet)
router.register(r'restaurant_images', views.Restaurant_imagesViewSet)
router.register(r'food_images', views.Food_imagesViewSet)


urlpatterns = [
   path('', include(router.urls)),
   path('register/', views.register_user, name='register_user'),
   path('login/', views.login_user, name='login_user'),
]
