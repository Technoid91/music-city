from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_lessons, name="lessons"),
    path('subscription/', views.check_subscription, name="check_subscription"),
    path('buy_subscription/<subscription_id>', views.buy_subscription, name="buy_subscription"),
]