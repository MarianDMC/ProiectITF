from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:beer_id>', views.beer_details, name='beer_details'),
    path('beers', views.all_beers, name='all_beers')
]