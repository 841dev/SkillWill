from django import forms
from .models import MemoryImage

class MemoryForm(forms.ModelForm):
    class Meta:
        model = MemoryImage
        fields = ['image']