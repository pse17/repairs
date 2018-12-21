''' Describe views application reports'''
from django.shortcuts import render

# Create your views here.

def index(request):
    ''' Home view'''
    return render(request, 'reports/index.html', context={})
