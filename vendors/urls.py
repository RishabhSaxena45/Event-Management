from django.urls import path
from vendors.views import *


urlpatterns = [
    path('' , loginuser , name='login'),
    path('register/' , registeruser , name='register'),
    path('home/' , home , name='home'),
    path('add/' , addproduct , name='add'),
    path('checkitem/' , checkitem , name='checkitem'),
    path('logout/' , logoutvendor , name='logoutvendor')
]
