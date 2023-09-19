# Generated by Django 4.2.4 on 2023-09-19 14:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('description', models.TextField(max_length=250, verbose_name='краткое описание')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='cover', verbose_name='обложка')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликован')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('authors', models.ManyToManyField(to='library_app.author', verbose_name='авторы')),
            ],
            options={
                'db_table': 'book',
                'ordering': ['-created_at'],
            },
        ),
    ]