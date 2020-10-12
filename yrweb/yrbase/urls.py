from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:id>/', views.newsfunc, name='newsfunc'), # `yrbase/5/`, 5 is an input from `newsfunc` in views.py
]
