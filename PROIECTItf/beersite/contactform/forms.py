from .models import Form

from django.forms import forms


class ContactForm(forms.Form):
    class Meta:
        model = Form
        fields = ['name', 'email', 'subject', 'message']

