from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def usluge(request):
    return render(request, 'home/usluge.html')

def novosti(request):
    return render(request, 'home/novosti.html')

def kontakt(request):
    return render(request, 'home/kontakt.html')