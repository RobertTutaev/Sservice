Активация виртуального окружения
======
myvenv\Scripts\activate

Создание виртуального окружения
======
python -m venv myvenv

Модели из DB
======
python manage.py inspectdb > smain/models.py

Выполнение migrate - создание таблиц в BD
======
python manage.py migrate

Создание migrate
======
python manage.py makemigrations

Установка Django
======
pip install --upgrade pip
pip install django~=1.11.0

Установка расширений
======
pip install mysqlclient

Версия Django
======
python -c "import django; print(django.get_version())"

Консоль Django (Django API)
======
python manage.py shell

Запуск web-сервера
======
python manage.py runserver

Создание суперпользователя
======
python manage.py createsuperuser

Полезные ссылки
======
https://rtfm.co.ua/django-primer-sozdaniya-prilozheniya-chast-1-sozdanie-zapusk-proekta/
https://habrahabr.ru/post/282874/
https://learn-reactjs.ru/basics/introduction-to-jsx
https://tutorial.djangogirls.org/ru/django_start_project/
https://habrahabr.ru/post/313764/