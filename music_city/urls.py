from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


handler404 = 'music_city.urls.custom_404_view'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('lessons/', include('lessons.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('newsletter/', include('newsletter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
