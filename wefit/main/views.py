from turtle import home
from django.shortcuts import render

#Function-based

# Home Page
def home(request):
    return render(request, 'home.html')
