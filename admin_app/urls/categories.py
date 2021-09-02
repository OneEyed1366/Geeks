import admin_app.views.categories as admin_app
from django.urls import path

app_name = "admin_app-categories"
urlpatterns = [
    path('create/', admin_app.CategoryCreateView.as_view(), name='create'),
    path('read/', admin_app.CategoryListView.as_view(), name='read'),
    path('update/<int:pk>/', admin_app.CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', admin_app.CategoryDeleteView.as_view(), name='delete'),
]
