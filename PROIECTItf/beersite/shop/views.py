from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import BeerTypes, Cart


# Create your views here.

def index(request):
    return render(request, "shop/index.html", )


def beer_details(request, beer_id):
    try:
        obj = BeerTypes.objects.get(id=beer_id)
        if request.method == 'POST':
            quantity = int(request.POST.get('quantity', 1))
            cart_item, created = Cart.objects.get_or_create(product=obj)
            if not created:
                cart_item.quantity += quantity
            cart_item.save()
            return redirect('cart')
    except BeerTypes.DoesNotExist:
        raise Http404(f'Berea cu id {beer_id} nu a fost gasita!')
    # return HttpResponse(f'You are looking at {obj}')
    return render(request, "shop/beer_details.html", {"obj": obj})


def all_beers(request):
    beer_list = BeerTypes.objects.all()
    return render(request, "shop/allbeers.html", {"beers": beer_list})

def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')

def cart_details(request):
    cart_items = Cart.objects.all()
    return render(request, 'shop/cart_details.html', {'cart_items': cart_items})
