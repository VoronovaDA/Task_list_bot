# Телеграм-бот для записи задач
## Стек: Python, Django, PostgreSQL

### Для работы с приложением клонируйте репозиторий:
```
git clone https://github.com/VoronovaDA/Task_list_bot.git

```
### Установите виртуальное окружение и зависимости:
```
python -m venv venv
```
```
venv/Scripts/activate
```
```
pip install -r requirements.txt
```
### В файле .env запишите свои данные PostgreSQL
### Создайте и проведите миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### Создайте суперюзера для админки:
```
python manage.py createsuperuser
```
### Запустите проект:
```
python manage.py runserver
```
### Ссылка на бота: 
```
t.me/Need_to_write_it_down_bot
```
