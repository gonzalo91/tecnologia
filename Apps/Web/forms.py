
from django import forms
from .models import Product, CollectionCenter
from django.utils.translation import gettext_lazy as _

class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)        
        self.fields['collection_center_id'].initial = 1
    
    class Meta:
        model = Product
        
        labels = {
            'name': _('Nombre'),
        }
        widgets= {'collection_center_id': forms.HiddenInput()}
        fields = "__all__"