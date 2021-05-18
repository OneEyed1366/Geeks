from django.urls import path
from . import views

app_name = "main_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('products/<str:slug>/', views.products, name='products-category'),
    path('product/<int:pk>/', views.products_sel, name='products-selected'),
    # path('products/sofa', views.products, name='products'),
    # path('products/chairs', views.products, name='products'),
    path('contact', views.contact, name='contact'),
]
