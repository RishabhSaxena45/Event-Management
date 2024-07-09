from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('' , loginuser , name='loginuser'),
    path('register/' , registeruser , name='registeruser'),
    path('home/' , adminhome)
]