from django import forms
from .models import categoryModel
class addcategory(forms.ModelForm):
    class Meta:
        model = categoryModel
        fields ="__all__"