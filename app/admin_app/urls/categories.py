import admin_app.views as admin_app
from django.urls import path

app_name = "admin_app-categories"
urlpatterns = [
    path('create/', admin_app.category_create, name='create'),
    path('read/', admin_app.categories, name='read'),
    path('update/<int:pk>/', admin_app.category_update, name='update'),
    path('delete/<int:pk>/', admin_app.category_delete, name='delete'),
]
