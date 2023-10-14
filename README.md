# Virtual_Library - виртуальная библиотека.

## Функционал проекта

### Книга

1. Просмотр списка книг
2. Просмотр детальной информации о книге
3. Поиск книг по названию или автору
4. Добавление, редактирование, удаление, создание книги
5. Api endpoints для списка книг
6. Api endpoints для детальной информации о книге
7. Пагинация для списка книг
8. Возможность добавить больше одного автора для книги
9. Автоматическое удаление данных из таблицы связь книги с авторами при удалении книги

### Автор

1. Добавление, редактирование, удаление, создание (только через админку django!)

### Комментарий

1. Возможность оставлять комментарии к книге

### Пользователь

1. Авторизация пользователя
2. Регистрация нового пользователя
3. Вход на сайт
4. Выход с сайта
5. Переброс на страницу 404

### Дополнительно

1. Тесты на TestCase
2. Команды для тестового заполнения базы данных
3. Использование Docker для развёртывания приложения

## Инструкция по запуску

### Работа с БД

Проект работает с postgresql, sqlite.

### Работа с docker-compose

1. Запуск сборки
    docker-compose up --build --remove-orphans
2. Остановка
    docker-compose down

### Работа с тестами

cd virtual_library
python manage.py test

По умолчанию в settings.py настройка бд использует :memory:

### Тестовое заполнение базы данных

cd virtual_library

1. Заполнение пользователей
    python manage.py filling_users --settings=virtual_library.local_settings
2. Заполнение библиотеки
    python manage.py filling_library --settings=virtual_library.local_settings

Используется local_settings для демонстрации заполнения

### Бэкап базы данных

python manage.py dumpdata > virtual_library.json --settings=virtual_library.local_settings

Это необходимо, если планируете загрузить данные для postgresql в docker

### Примечание

Строка в docker-compose.yaml

&& python manage.py loaddata --settings=virtual_library.prod_settings virtual_library.json

Эта строка сохраняет данные бэкапа в базу данных
Её можно убрать, если вы не планируете грузить данные в postgresql внутри docker