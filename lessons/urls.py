from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_lessons, name="lessons"),
    path('subscription/', views.check_subscription, name="check_subscription"),
    path('subscribe/<int:subscription_id>/', views.purchase_subscription, name="purchase_subscription"),
]