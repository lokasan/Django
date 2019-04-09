from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


def main(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, 'mainapp/index.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Главная', 'prod_cat': prod_cat})
    

def catalogue(request, pk=None):
    print(pk)
    prod_cat = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            prod_cat_all = {'name': 'Все'}
        else:
            prod_cat_all = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        return render(request, 'mainapp/catalogue/products_list.html', context={'user': request.user,
                                                                        'menu': {'main': 'Главная',
                                                                                 'catalogue': 'Каталог',
                                                                                 'contacts': 'Контакты'},
                                                                        'page': 'Каталог', 'products': products,
                                                                        'prod_cat_all': prod_cat_all, 'prod_cat': prod_cat, 'basket': basket})

    same_products = Product.objects.all()
    return render(request, 'mainapp/catalogue/index.html', context={'user': request.user,
                                                                    'menu': {'main': 'Главная',
                                                                             'catalogue': 'Каталог',
                                                                             'contacts': 'Контакты'},
                                                                    'page': 'Каталог',
                                                                    'products': same_products, 'prod_cat': prod_cat})


def contacts(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, 'mainapp/contacts/index.html', context={'user': request.user, 'placeholder': {'name': 'ivan', 'email': 'mail@gmail.com', 'theme': 'покупка монитора'}, 'prod_cat': prod_cat, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'page': 'Контакты'})


def monitor(request):
    prod_cat = ProductCategory.objects.all()
    return render(request, r'mainapp/catalogue/monitor/Eizo ColorEdge CG318-4K/CG318-4K.html', context={'user': request.user, 'menu': {'main': 'Главная', 'catalogue': 'Каталог', 'contacts': 'Контакты'}, 'prod_cat': prod_cat})
# Create your views here.

# Create your views here.
