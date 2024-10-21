from django import forms
# from .widgets import CustomClearableFileInput
from .models import Product, Category, PreviewImage

class ProductForm(forms.ModelForm):
    
    images = forms.ImageField (
        label='Preview Images',
        required=False
        
    )
    class Meta:
        model = Product
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            categories = Category.objects.all()
            friendly_names = [(c.id, c.get_friendly_name()) for c in 
            categories]
            self.fields['category'].choices = friendly_names

            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'

    def save(self, commit=True):
        
        product_instance = super().save(commit=commit)
        
        return product_instance

