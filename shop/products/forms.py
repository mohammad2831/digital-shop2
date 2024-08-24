from django import forms
from .models import Products, ProductAttribute
import base64

class ProductsForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Products
        
        fields = ['type','category', 'name', 'slug','image','description', 'price', 'available', 'stock']
    def save(self, commit=True):
        instance = super(ProductsForm, self).save(commit=False)
        if self.cleaned_data.get('image'):
            image_file = self.cleaned_data['image']
            instance.image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
        if commit:
            instance.save()
        return instance

    
class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = ['attribute', 'value']