import admin_app.views as admin_app
from django.urls import path

app_name = "admin_app-products"
urlpatterns = [
    path('read/category/<int:pk>/', admin_app.products, name='index'),
    path('create/category/<int:pk>/', admin_app.product_create, name='create'),
    path('read/<int:pk>/', admin_app.product_read, name='read'),
    path('update/<int:pk>/', admin_app.product_update, name='update'),
    path('delete/<int:pk>/', admin_app.product_delete, name='delete'),
]
