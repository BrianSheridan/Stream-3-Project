from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from django.template.context_processors import csrf


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})




