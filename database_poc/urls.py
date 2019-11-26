from django.urls import path
from . import views

urlpatterns = [
    # /test/
    path('', views.testpage.as_view(), name='test'),

    #/test/datainput
    path('datainput/', views.datainput.as_view(), name='datainput'),

    #/test/dataoutput
    path('dataoutput/', views.dataoutput.as_view(), name='dataoutput')
]