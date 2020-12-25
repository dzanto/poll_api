# poll_api
API для системы опросов пользователей

###### Установка:
1. Склонируйте репозиторий
2. Создайте и войдите в вирутальное окружение
3. Установите зависимости:
    - `pip install -r requirements.txt`
4. Проведите миграции
    - `python manage.py makemigrations`
    - `python manage.py migrate`
5. Создайте суперпользователя
    - `python manage.py createsuperuser`
6. Запустите тестовый сервер
    - `python manage.py runserver`
