from . import views
from django.urls import path

app_name = 'yrbase'  # used for html `{% url "yrbase:home" %}` etc.

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('donate/', views.Donate, name='donate'),
]
