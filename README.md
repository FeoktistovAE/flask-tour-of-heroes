## Описание:

Тур героев - это образовательный REST API проект, который представляет из себя круд для работы с моделью "Герои", выполненный с помощmю микрофреймворка Flask.

## Stack:

* Flask-SQLAlchemy
* Flask-RESTful
* flask-marshmallow
* Flask-Alembic

### Установка:

Склонируйте репозиторий:
```bash
git clone https://github.com/FeoktistovAE/flask-tour-of-heroes
```

Войдите в корневую папку:
```bash
cd flask-tour-of-heroes
```

Установите зависимости c помощью Poetry:
```bash
make install
```

Измените имя файла .env.sample на .env:
```bash
mv .env.sample .env
```

Добавьте все необходимые переменные окружения для конфигурации базы данных в файл .env, например так:
```bash
DATABASE = 'postgresql'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = '123'
HOST = 'localhost'
DATABASE_NAME = 'heroes'
```

Запустите приложение:
```bash
make start
```
