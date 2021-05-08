from django.core.management.base import BaseCommand, CommandError
from auth_app.models import User

class Command(BaseCommand):
    help = "Обновление списка пользователей"

    def handle(self, *args, **kwargs):
        User().configure()