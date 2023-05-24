from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')