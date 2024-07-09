from django.urls import path
from User.views import *

urlpatterns = [
    path('' , loginuser , name='loginuser'),
    path('register/' , registeruser , name='registeruser'),
    path('home/' , home , name='home'),
    path('addevent/' , addevent , name='addevent'),
    path('cart/' , cartlist , name='cartlist'),
    path('guest/' , addguest , name='addguest'),
    path('logout/' , logoutuser , name='logout')
]
