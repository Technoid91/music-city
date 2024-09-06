from django.urls import path
from .import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('create-letter/', views.send_newsletter, name='send_newsletter'),
    ]
