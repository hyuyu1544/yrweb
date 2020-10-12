from django.shortcuts import render

# Create your views here.


def index(request):
    """Index"""
    return render(request, 'yrbase/index.html')
