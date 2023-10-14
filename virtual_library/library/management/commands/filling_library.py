from django.core.management.base import BaseCommand
from django.utils.timezone import now
from factory.django import DjangoModelFactory
from factory import Faker
from library.models import Book, Author, Comment
from accounts.management.commands.filling_users import UserFactory


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = Faker('name')
    birthday = Faker('date')
    short_biography = Faker('text', max_nb_chars=250)


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = Faker('sentence', nb_words=2)
    year = now().year
    description = Faker('text', max_nb_chars=350)
    is_published = Faker('boolean')


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    
    text = Faker('text')
    is_published = Faker('boolean')


class Command(BaseCommand):
    help = 'команда создаст тестовые книги с их авторами'
    
    def handle(self, *args, **kwargs):
        try:
            for _ in range(0, 16):
                author_1 = AuthorFactory()
                author_2 = AuthorFactory()
                book = BookFactory()
                book.authors.set([author_1, author_2])
                user = UserFactory()
                CommentFactory(book=book, user=user)
        except Exception as err:
            print(err)
        self.stdout.write(self.style.SUCCESS('Успешное тестовое заполнение таблиц: author, book, users, comment!'))
