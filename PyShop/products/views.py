from django.shortcuts import render
from django.http import HttpResponse
from .models import Product as p

# Create your views here.

def index(request):
    products = p.objects.all()
    return render(request,'index.html',
                    {'products' : products})


def new(request):
    return HttpResponse('<h1>Welcome New Product</h1>')


