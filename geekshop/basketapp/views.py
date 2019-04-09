from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    content = {'korzina': basket()}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = request.user.basket.filter(product=pk).first()

    if basket:
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
