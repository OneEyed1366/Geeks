import admin_app.views as admin_app
from django.urls import path

app_name = "admin_app-users"
urlpatterns = [
    path('create/', admin_app.user_create, name='create'),
    path('read/', admin_app.users, name='read'),
    path('update/<int:pk>/', admin_app.user_update, name='update'),
    path('delete/<int:pk>/', admin_app.user_delete, name='delete'),
]
