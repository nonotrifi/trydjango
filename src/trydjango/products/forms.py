from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
        
        
class RawProduct(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=False)
    price = forms.DecimalField( )
    
        