"""
Main URLs
"""
from django.urls import path

from app_main import views, ajax

app_name = 'app_main'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('post/login/', ajax.post_login, name='post_login'),
    path('post/register/', ajax.post_register, name='post_register'),
]
