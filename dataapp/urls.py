from django.urls import path
from . import views


urlpatterns = [
    
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('add_service/', views.add_service, name='add_service'),
    
]
