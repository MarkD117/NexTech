from django import forms
from .models import Subscriber

class NesletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']