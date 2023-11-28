from django import forms
from .models import Logger

# Create your models here.
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        