from django import forms
from .models import Service
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Existing ServiceForm
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'start_date', 'first_payment_date', 'renewal_type', 'auto_renew', 'auto_renew_date', 'custom_notes']

