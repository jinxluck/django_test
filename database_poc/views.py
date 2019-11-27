from django.shortcuts import render, redirect
from .models import testdatabase
from .forms import TestForm
from django.views import View

# Create your views here.
#/test/
class testpage(View):

    def get(self, request):
        return render(request, 'database_poc/test.html')

#/test/datainput/
class datainput(View):

    #get requesten til indlæsning af siden, hvor "formen" TestForm definere tekstfelt og tick boksen
    def get(self, request):
        form = TestForm()
        return render(request, 'database_poc/datainput.html', {'form':form})

    #post requesten det bliver givet nå man trykker på knappen "submit"
    def post(self, request):
        form = TestForm(request.POST)
        #gemmer inputtene hvis de er "valide"
        if form.is_valid():
            form.save()
            return redirect('/test/')

        #i tilfælde af "invalide" input eks. blankt tekstfelt
        return render(request, 'database_poc/datainput.html', {'form':form})

class dataoutput(View):

    # get requesten til indlæsning af siden, som henter objekterne fra databasen, så de kan blive vist på siden
    def get(self, request):
        all_data = testdatabase.objects.all()
        return render(request, 'database_poc/dataoutput.html', {'all_data': all_data})