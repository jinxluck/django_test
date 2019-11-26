from django.urls import path
from . import views

urlpatterns = [
    # /index/
    path('', views.index, name='albums'),

    # /index/id_number/
    path('<int:album_id>/', views.detail, name='detail')
]