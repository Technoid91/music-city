from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_lessons, name="lessons"),
    path('lesson/<lesson_id>',
         views.lesson, name="lesson"),
    path('subscription/',
         views.check_subscription, name="check_subscription"),
    path('buy_subscription/<subscription_id>',
         views.buy_subscription, name="buy_subscription"),
    path('new_lesson/',
         views.add_lesson, name='add_lesson'),
    path('edit_lesson/<int:lesson_id>/',
         views.edit_lesson, name='edit_lesson'),
    path('delete_lesson/<int:lesson_id>/',
         views.delete_lesson, name='delete_lesson'),
    path('add_playlist/',
         views.add_playlist, name='add_playlist'),
    path('delete_playlist/<int:playlist_id>/',
         views.delete_playlist, name='delete_playlist'),
    path('add_subscription/',
         views.add_subscription, name='add_subscription'),
    path('edit_subscription/<int:subscription_id>/',
         views.edit_subscription, name='edit_subscription'),
    path('delete_subscription/<int:subscription_id>/',
         views.delete_subscription, name='delete_subscription'),
]
