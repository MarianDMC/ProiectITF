from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, redirect


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact_success')


    else:
        form = ContactForm()

    return render(request, 'shop/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'shop/success.html')
