from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name="home"),
    path('password/', views.password, name="Password"),
    
]