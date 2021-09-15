from django.shortcuts import render
from .models import product
# Create your views here.


def home(request):
    context = {'products': product.objects.all()}
    print("----------->", product.objects.all())
    return render(request, 'store/home.html', context)


def cart(request):
    return render(request, 'store/cart.html')
