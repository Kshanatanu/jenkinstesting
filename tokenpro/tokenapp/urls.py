# this is new comeent on the file
from django.urls import path
from .mylogics import login 

urlpatterns = [
    path('',login.hello),
]
