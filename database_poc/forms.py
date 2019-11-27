from django import forms
from .models import testdatabase

#forms er blevet brugt for at gøre get/post requestes nemmere at håndtere
class TestForm(forms.ModelForm):
    Data = forms.CharField()
    NODELETE = forms.CheckboxInput()

    #meta class for at associere formen "TestForm" med modellen "testdatabase"
    class Meta:
        model = testdatabase
        fields = ('Data','NODELETE')