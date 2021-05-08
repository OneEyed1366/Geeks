from django.db import models
from django.contrib.auth.models import AbstractUser
from os import path
from json import load
from random import randrange


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

    def configure(self):
        with open(path.join(
            "media",
            "bd",
            "users.json"
        ), "r+", encoding="utf-8") as f:
            users = load(f)

        User.objects.create_superuser(
            "Admin",
            "coolAdmin@mail.ru",
            "adminAwesomd",
            age = "25",
            first_name="KKi",
            desc="Best admin in the world!",
            )

        for user_id in users:
            _id = user_id
            data = {
                "username": users[_id]["username"],
                "password": users[_id]["password"],
                "email": users[_id]["email"],
                "first_name": users[_id]["first_name"],
                "desc": users[_id]["desc"],
                "age": users[_id]["age"],
            }

            User.objects.update_or_create(
                id=_id,
                defaults=data,
            )
