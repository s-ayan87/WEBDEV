from django.shortcuts import render

def index(request):
    return render(request, 'maps/index.html')

def home(request):
    return render(request, 'maps/home.html')