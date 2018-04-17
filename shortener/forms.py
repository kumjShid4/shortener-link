from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = URL
        fields = ('url',)
        widgets = {
            'url': forms.URLInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Your original url here'})
        }