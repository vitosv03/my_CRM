from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewIndex, name='index')
]
