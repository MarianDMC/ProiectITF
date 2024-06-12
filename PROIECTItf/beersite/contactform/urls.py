from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path('success', views.contact_success, name='success')
]