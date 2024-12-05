from django.urls import path
from food.views import *
app_name='fooditems'
urlpatterns=[
    path('veg/',veg,name='veg'),
]
