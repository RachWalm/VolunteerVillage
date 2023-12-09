from django.shortcuts import render

# Create your views here.

def pending(request):
    return render(request, 'coordinator/pending.html')

def home(request):
    return render(request, 'index.html')