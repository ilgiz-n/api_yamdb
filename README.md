# API проекта YaMDb

### Описание проекта:
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). 

Текущая версяи API: v1.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ilgiz-n/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

Получить список основных эндпоинтов:

```
http://127.0.0.1:8000/api/v1/
```

Для аутентификации используются JWT-токены.
Для регистраци необходимо 
1. Получить код подтверждения на указанную почту.
Необходимо отправить POST запрос к эндопоинту

```
http://127.0.0.1:8000/api/v1/signup/
```

в формате:

```
{
  "username": "вашлогин",
  "email": "from@example.com"
}

```

2. Далее для получения токена, необходимо полученный по почте код подтверждения отправить в POST запросе к эндопоинту:


```
http://127.0.0.1:8000/api/v1/token/
```

в формате:

```
{
  "username": "вашлогин",
  "confirmation_code": "000000"
}
```

Полный перечень типов запросов представлен
в документации к API в формате Redoc в адресу:

```
http://127.0.0.1:8000/redoc/
```

### Cистемные требования 
 - Python 3.7.3
 - Django 2.2.16
 - Django REST framework 3.12.4
 - requests, djangorestframework-simplejwt, django-filter, PyJWT, pytest, pytest-django, pytest-pythonpath, psycopg2-binary

### Разработка проекта: 

[Ильгиз Нигматуллин](https://github.com/ilgiz-n) - вся часть, касающуюся управления пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail.

[Екатерина Русова](https://github.com/Rukate) - категории (Categories), жанры (Genres) и произведения (Titles): модели, представления и эндпойнты для них.

[Никита Макареичев](https://github.com/NikitaMakareichev) - отзывы (Review) и комментари (Comments): описание моделей, представлений, настройка эндпойнтов, определение прав доступа для запросов. Рейтинги произведений.
