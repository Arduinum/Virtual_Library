from django.core.management.base import BaseCommand
from factory.django import DjangoModelFactory
from factory import Faker
from accounts.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('name')
    is_active = Faker('boolean')
    email = Faker('email')
    password = Faker('password')


class Command(BaseCommand):
    help = 'команда создаст тестовых пользователей'

    def handle(self, *args, **kwargs):
        try:
            UserFactory.create_batch(15)
        except Exception as err:
            print(err)

        self.stdout.write(self.style.SUCCESS('Успешное тестовое заполнение таблицы users!'))
