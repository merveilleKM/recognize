from django import forms
from .models import ImageRecognition

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageRecognition
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }