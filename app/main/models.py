from django.db import models
from os import path
from json import load

class Product(models.Model):
    img_hero = models.ImageField(blank=True, upload_to=path.join(
        'img',
        'products',
    ))
    text_title = models.CharField(max_length=100)
    text_desc = models.CharField(max_length=100)

    def __str__(self):
        return f"Карточка товара -> {self.text_title}"

    def configure(self):
        with open(path.join(
            'media',
            'bd',
            'products.json'
        ), "r+", encoding="utf-8") as f:
            products = load(f)

        for product_id in products:
            number_id = product_id
            data = {
                "text_title": products[product_id]["title"],
                "text_desc": products[product_id]["desc"],
            }

            Product.objects.update_or_create(
                    id = number_id,
                    defaults = data
                    )
