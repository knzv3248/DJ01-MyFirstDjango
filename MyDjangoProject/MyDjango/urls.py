from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data', views.my_data),
    path('test', views.my_test),
]
