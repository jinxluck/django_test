from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # /test/
    path('', views.index, name='albums'),

    # /test/id_number/
    path('<int:album_id>/', views.detail, name='detail')
]