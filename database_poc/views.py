from django.shortcuts import render, redirect
from .models import testdatabase
from .forms import TestForm
from django.views import View

# Create your views here.
#/test/

class testpage(View):

    def get(self, request):
        return render(request, 'database_poc/test.html')


class datainput(View):

    def get(self, request):
        form = TestForm()
        return render(request, 'database_poc/datainput.html', {'form':form})

    def post(self, request):
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['Data']
            form = TestForm()
            return redirect('/test/')

        args = {'form':form, 'text': text}
        return render(request, 'database_poc/datainput.html', args)

class dataoutput(View):

    def get(self, request):
        all_data = testdatabase.objects.all()
        return render(request, 'database_poc/dataoutput.html', {'all_data': all_data})