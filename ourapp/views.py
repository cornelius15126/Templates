from django.shortcuts import render
from django.http import HttpResponse
from .models import features

# Create your views here./*
def index(request):
    features = features.object.all()
  

    return render(request, 'index.html', {'feature': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})