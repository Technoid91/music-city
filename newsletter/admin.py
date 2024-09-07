from django.contrib import admin
from .models import NewsSubscriber


# Register your models here.
class NewsSubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
    )


admin.site.register(NewsSubscriber, NewsSubscriberAdmin)
