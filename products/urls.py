from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_products, name="products"),
    path('<product_id>/', views.product_detail, name="product_detail"),
]
