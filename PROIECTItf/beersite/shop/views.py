from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import BeerTypes


# Create your views here.

def index(request):
    return render(request, "shop/index.html",)

def beer_details(request, beer_id):
    try:
        obj = BeerTypes.objects.get(id=beer_id)
    except BeerTypes.DoesNotExist:
        raise Http404(f'Berea cu id {beer_id} nu a fost gasita!')
    #return HttpResponse(f'You are looking at {obj}')
    return render(request, "shop/beer_details.html", {"obj": obj})

def all_beers(request):
    beer_list = BeerTypes.objects.all()
    return render(request, "shop/allbeers.html", {"beers": beer_list})
