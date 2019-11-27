from django.urls import path
from . import views

#hvilke URL stier der tilhører denne app, og hvilket "view" der skal findes til pågældende URL
urlpatterns = [
    # /test/
    path('', views.testpage.as_view(), name='test'),

    #/test/datainput
    path('datainput/', views.datainput.as_view(), name='datainput'),

    #/test/dataoutput
    path('dataoutput/', views.dataoutput.as_view(), name='dataoutput')
]