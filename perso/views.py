from django.shortcuts import render

def index(request):
    return render(request, 'perso/home.html')

# Create your views here.
