from django.urls import path
from .views import *


urlpatterns =[
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('post/',post_blog),
    path('display/',display),
    path('publish/',publish),

    
]