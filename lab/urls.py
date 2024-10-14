from django.urls import path
from . import views


urlpatterns = [
    path('sergei', views.index, name='home'),
    path('webApp', views.webApp, name='webApp'),
    path('chatBot', views.chatBot, name='chatBot'),
    path('ML', views.ML, name='ML'),
    path('Games', views.Games, name='Games'),
    path('tester', views.tester, name='tester'),
    path('casper', views.casper, name='casper'),
    path('', views.sergei, name='sergei'),
]
