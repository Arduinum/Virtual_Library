from django.test import TestCase
from django.utils.timezone import now
from factory.django import DjangoModelFactory
from factory import Faker
from library.models import Book, Author, Comment
from accounts.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker('name')
    is_active = Faker('boolean')
    email = Faker('email')
    password = Faker('password')


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


class LibraryTest(TestCase):
    "Тестирует весь функционал библиотеки"

    def setUp(self):
        self.author_1 = AuthorFactory()
        self.author_2 = AuthorFactory()
        self.book = BookFactory()
        self.book.authors.set([self.author_1, self.author_2])
        self.user = UserFactory()
        self.comment = CommentFactory(book=self.book, user=self.user)
    
    def test_author_is_created(self):
        """проверка на соответствие классу Author"""
        self.assertEqual(str(type(self.author_1)), "<class 'library.models.Author'>")
    
    def test_book_is_created(self):
        """проверка на соответствие классу Book"""
        self.assertEqual(str(type(self.book)), "<class 'library.models.Book'>")

    def test_user_is_created(self):
        """проверка на соответствие классу User"""
        self.assertEqual(str(type(self.user)), "<class 'accounts.models.User'>")
    
    def test_comment_is_created(self):
        """проверка на соответствие классу Comment"""
        self.assertEqual(str(type(self.comment)), "<class 'library.models.Comment'>")

    def test_author_is_data_fields(self):
        """проверит существуют ли данные в Author"""
        if self.author_1.name and self.author_1.birthday and self.author_1.short_biography:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_author_is_data_book(self):
        """проверит существуют ли данные в Book"""
        if self.book.title and self.book.year and self.book.description:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_author_is_data_user(self):
        """проверит существуют ли данные в User"""
        if self.user.username and self.user.email and self.user.password:
            self.assertTrue(True)
        else:
            self.assertTrue(False)  
    
    def test_author_is_data_comment(self):
        """проверит существуют ли данные в Comment"""
        if self.comment.text:
            self.assertTrue(True)
        else:
            self.assertTrue(False)  

    def test_book_published_is_bool(self):
        """проверит имеет ли тип bool поле is_published в Book"""
        self.assertEqual(str(type(self.book.is_published)), "<class 'bool'>")
    
    def test_user_published_is_bool(self):
        """проверит имеет ли тип bool поле is_active в User"""
        self.assertEqual(str(type(self.user.is_active)), "<class 'bool'>")

    def test_comment_published_is_bool(self):
        """проверит имеет ли тип bool поле is_published в Comment"""
        self.assertEqual(str(type(self.comment.is_published)), "<class 'bool'>")
