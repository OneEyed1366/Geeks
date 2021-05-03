from django.core.management.base import BaseCommand, CommandError
from main.models import Products

class Command(BaseCommand):
    help = "Обновление линейки представленных на сайте товаров"

    def handle(self, *args, **kwargs):
        Products().configure()