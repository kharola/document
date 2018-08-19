from django import forms

from .models import FileSys

class FileSysForms(forms.ModelForm):
    class Meta:
        model = FileSys
        fields = '__all__'
