from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import now


class Author(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=100,
        blank=False,
        null=False
    )

    birthday = models.DateField(
        verbose_name='дата рождения',
        blank=False,
        null=False
    )

    short_biography = models.TextField(
        verbose_name='краткая биография',
        max_length=250,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='дата обновления',
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=100,
        blank=False,
        null=False
    )

    authors = models.ManyToManyField(
        to=Author,
        verbose_name='авторы'
    )

    year = models.IntegerField(
        verbose_name='год издания',
        validators=[
            MaxValueValidator(now().year)
        ],
        blank=False,
        null=False
    )

    description = models.TextField(
        verbose_name='краткое описание',
        max_length=250,
        blank=False,
        null=False
    )

    cover = models.ImageField(
        verbose_name='обложка',
        upload_to='cover',
        blank=True,
        null=True
    )

    is_published = models.BooleanField(
        verbose_name='опубликован',
        default=False
    )

    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='дата обновления',
        auto_now=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'book'
        ordering = ['-created_at']
