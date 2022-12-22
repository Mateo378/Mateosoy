from django.urls import path
from CoreApp import views

urlpatterns = [
    path('', views.home, name="info"),
]