from django.shortcuts import render, redirect
from .models import Users, Restaurant
from .forms import UserRegistrationForm, RestaurantRegistrationForm

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')  # O'zingizning bosh sahifangizga o'ting
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def restaurant_registration(request):
    if request.method == 'POST':
        form = RestaurantRegistrationForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.password = make_password(form.cleaned_data['password'])
            restaurant.save()
            return redirect('home')  # O'zingizning bosh sahifangizga o'ting
    else:
        form = RestaurantRegistrationForm()
    return render(request, 'restaurant_registration.html', {'form': form})
