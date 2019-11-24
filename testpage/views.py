from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import album, song

def index(request):
    all_albums = album.objects.all()
    return render(request, 'testpage/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    albums = get_object_or_404(album, pk=album_id)
    return render(request, 'testpage/detail.html', {"albums": albums})
