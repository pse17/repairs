''' Describe URLs for application reports'''
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index')
]
