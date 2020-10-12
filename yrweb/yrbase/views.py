# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    """Index"""
    return render(request, 'yrbase/home.html', {'title': 'Home | YR'})


def About(request):
    """About"""
    return render(request, 'yrbase/about.html', {'title': 'About | YR'})


def Donate(request):
    """About"""
    return render(request, 'yrbase/donate.html', {'title': 'Donate | YR'})
