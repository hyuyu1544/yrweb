from . import views
from django.urls import path


urlpatterns = [
    path('home/', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('donate/', views.Donate, name='donate'),
]
