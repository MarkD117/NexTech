from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, ProductCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # Replace image field on form to use custom image widget
    image = forms.ImageField(
        label='Image',required=False, widget=CustomClearableFileInput)

    # Override init method to make changes to the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = ProductCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-form-input'
