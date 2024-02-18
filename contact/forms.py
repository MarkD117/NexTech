from django import forms
from .models import NewsletterSubscriber, Contact

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your email'})


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'contact-form-input'
