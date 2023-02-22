
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.cityMetod, name='city'),
    path('createcity', views.createcity, name='createcity'),
    path('deletecity', views.deletecity, name='deletecity'),
    path('<int:pk>/deletetemp', views.deletetemp, name='deletetemp'),
    path('temp', views.tempMetod, name='temp'),
    path('createtemp', views.createtemp, name='createtemp'),
    path('chart', views.findtemp, name='chart'),

]