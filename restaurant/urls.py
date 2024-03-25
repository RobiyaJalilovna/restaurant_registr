from django.urls import path
from . import views

urlpatterns = [
    path('register/user/', views.user_registration, name='user_registration'),
    path('register/restaurant/', views.restaurant_registration, name='restaurant_registration'),
]
