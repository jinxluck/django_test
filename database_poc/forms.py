from django import forms
from .models import testdatabase

class TestForm(forms.ModelForm):
    Data = forms.CharField()

    class Meta:
        model = testdatabase
        fields = ('Data',)