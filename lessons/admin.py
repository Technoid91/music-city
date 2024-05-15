from django.contrib import admin
from .models import Subscription, UserSubscription, Lesson, Playlist


class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subscribed',
        'subscription_name',
        'start_date',
        'expiry_date',
    )

    ordering = ('subscribed', 'start_date')



class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'playlist',
        'number',
        'name',
    )

    ordering= ('playlist', 'number',)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Subscription)
admin.site.register(UserSubscription, UserSubscriptionAdmin)
