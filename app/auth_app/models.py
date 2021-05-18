from django.db import models
from django.contrib.auth.models import AbstractUser
from os import path


class User(AbstractUser):
    avatar = models.ImageField(verbose_name = "Аватарка",
        blank=True, upload_to=path.join("img", "users", "avatars"))
    username = models.CharField(blank = True, unique = True, verbose_name = "Ник", max_length=250)
    email = models.EmailField(blank = True, verbose_name = "eMail")
    first_name = models.CharField(verbose_name = "ФИО", max_length=250)
    desc = models.CharField(verbose_name= "описание", max_length=400)
    age = models.PositiveIntegerField(verbose_name = "возраст")

    def __str__(self):
        return f"Пользователь: {self.username} (Имя: {self.first_name}, возраст: {self.age})"