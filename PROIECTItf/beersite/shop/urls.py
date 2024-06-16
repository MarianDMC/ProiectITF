from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('cart', views.cart_details, name='cart'),
    path('beers', views.all_beers, name='all_beers'),
    path("shop/", views.index, name="index"),
    path('<int:beer_id>', views.beer_details, name='beer_details'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
