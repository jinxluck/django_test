from django import forms
from .models import testdatabase

class TestForm(forms.ModelForm):
    Data = forms.CharField()
    NODELETE = forms.CheckboxInput()

    class Meta:
        model = testdatabase
        fields = ('Data','NODELETE')