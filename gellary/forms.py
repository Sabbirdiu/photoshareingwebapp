from django import forms
from .models import ImageAlbum


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = ImageAlbum
        fields = '__all__'