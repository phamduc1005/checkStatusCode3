from django.urls import path
from . import views

urlpatterns = [
    # path('<str:nameTest>', views.testUrlsFromSitemaps, name="testUrlsFromSitemaps"),
    # path('all checks of a website/<str:nameTest>', views.allCheck, name="allCheckAWeb"),
    path('allChecksOfAWebsite/<str:nameTest>/', views.checksAllUrlErrorOfAWeb, name='allChecksOfACebsite'),
    path('lastCheckOfEachWebsite/', views.checkOfAWebsite, name='lastCheckOfEachWebsite'),
    path('checkLastUrlAllError/', views.checkLastUrlAllError, name='checkLastUrlAllError'),
]
