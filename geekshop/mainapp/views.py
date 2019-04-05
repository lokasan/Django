from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, 'mainapp/index.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Главная', 'prod_cat': prod_cat})
    

def catalogue(request, pk=None):
    products = Product.objects.all()
    prod_cat =ProductCategory.objects.all()
    return render(request, 'mainapp/catalogue/index.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Каталог', 'products': products, 'prod_cat': prod_cat})
    

def contacts(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, 'mainapp/contacts/index.html', context={'user': request.user, 'placeholder': {'name': 'ivan', 'email': 'mail@gmail.com', 'theme': 'покупка монитора'}, 'prod_cat': prod_cat, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Контакты'})


def monitor(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, r'mainapp/catalogue/monitor/Eizo ColorEdge CG318-4K/CG318-4K.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'prod_cat': prod_cat})
# Create your views here.

# Create your views here.
