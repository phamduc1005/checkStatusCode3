from django.urls import path
from . import views

urlpatterns = [
    path('lastCheckOfEachWebsite/', views.checkOfAWebsite, name='lastCheckOfEachWebsite'),
    path('checkLastUrlAllError/', views.checkLastUrlAllError, name='checkLastUrlAllError'),
    path('allChecksOfAWebsite/<str:nameTest>/', views.checksAllUrlErrorOfAWeb, name='allChecksOfACebsite'),
]
