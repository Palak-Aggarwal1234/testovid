from django import forms
from .models import ReportDb, Image

class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportDb
        fields = ['Test1', 'Test2', 'Owner']


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ['title', 'image', 'Owner']