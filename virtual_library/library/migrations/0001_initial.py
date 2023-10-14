# Generated by Django 4.2.4 on 2023-10-12 08:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('birthday', models.DateField(verbose_name='дата рождения')),
                ('short_biography', models.TextField(max_length=250, verbose_name='краткая биография')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2023)], verbose_name='год издания')),
                ('description', models.TextField(max_length=350, verbose_name='краткое описание')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='cover', verbose_name='обложка')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликован')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('authors', models.ManyToManyField(to='library.author', verbose_name='авторы')),
            ],
            options={
                'db_table': 'book',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='комментарий')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликован')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='книга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'db_table': 'comment',
                'ordering': ['-created_at'],
            },
        ),
    ]
