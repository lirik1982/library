<h1>ТЕСТОВОЕ ЗАДАНИЕ на позицию 
Junior Python разработчик 
</h1>
<br>

В задании описан сервис работы библиотеки с 2 вариантами пользователей (читатель/библиотекарь).<br>
Должен быть реализован механизм авторизации.<br>
Читатели должны иметь возможность взять/сдать книгу,<br> 
библиоткарь - смотреть должников.<br>
<br>
Также, должна быть возможность выполнить ряд операций через DRF с JWT.
<br>
<br>
## 🛠️ Для установки и запуска сервиса, нужно выполнить следующие действия:

- склонируйте текущий репозиторий в локальную папку и выполните команду:
 ```cmd
    git clone https://github.com/lirik1982/library.git
```
- перейдите в папку импортированного репозитория и наберите в командной строке (в системе должна быть установлена программная платформа Docker):
```cmd
    docker-compose up -d
```
- будет выполнено развертывание docker-контейнеров с настроенным образом:
  - django/drf
  <br>суперпользователь - test@mail.com/123
  <br>библиотекарь - librarian1@mail.ru/!Qwerty1
  <br>читатель 1 - reader1@mail.ru/!Qwerty1
  <br>читатель 2 - reader2@mail.ru/!Qwerty1

- сервис готов к обработке запросов

Страничный Интерфейс понятен интуитивно, и доступен по адресу: http://localhost:8000/


## 🗃️ Обработка API запросов:
<br>
<h3>Для авторизации</h3>
* Для отправки данных для обработки, необходимо выполнить POST-запрос с телом, с данными пользователя:
 
```cmd
    curl --location 'localhost:8000/api/users/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user": {
        "email": "reader1@mail.ru",
        "password": "!Qwerty1"
    }
}'

```

Будет получен ответ вида:
 ```cmd
{
    "user": {
        "email": "reader1@mail.ru",
        "username": "reader1",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwiZXhwIjoxNzIyNTAyOTM2fQ.haSeeMybF_TPKtjvA6NC7E-je-Yo0oWlhCZf8HaOMLc"
    }
}
```

Значение токена, нужно скопировать в буфер обмена, для использования в последующих запросах


<br>
<h3>Для получения списка книг</h3>
* Для отправки данных для обработки, необходимо выполнить GET-запрос с<br>
вариантом авторизации Authorization: Bearer и токеном, полученным, при авторизации

```cmd
  curl --location 'localhost:8000/api/books/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwiZXhwIjoxNzIyNTAyOTM2fQ.haSeeMybF_TPKtjvA6NC7E-je-Yo0oWlhCZf8HaOMLc' \
--data ''

```

Будет получен ответ вида:
 ```cmd
...
"list": [
            {
                "id": 1,
                "title": "Машина времени",
                "author": "Герберт Уэлс",
                "genre": "научная фантастика"
            },
            {
                "id": 2,
                "title": "Автостопом по галактике",
                "author": "Дуглас Адамс",
                "genre": "научная фантастика"
            },
            {
...
```

<br>
<h3>Для взятия книги из библиотеки</h3>
* Для отправки данных для обработки, необходимо выполнить GET-запрос с<br>
вариантом авторизации Authorization: Bearer и токеном, полученным, при авторизации

```cmd
 curl --location 'localhost:8000/api/take_book/<N>' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwiZXhwIjoxNzIyNTAyOTM2fQ.haSeeMybF_TPKtjvA6NC7E-je-Yo0oWlhCZf8HaOMLc' \
--data ''
```
Вместо <N> следует указать ID желаемой книги.

Будет получен ответ вида:
 ```cmd
...
{
    "user": {
        "Операция": "Успешно"
    }
}

ИЛИ

{
    "user": {
        "Операция": "Неудача"
    }
}
```

<br>
<h3>Для возврата книги в библиотеку</h3>
* Для отправки данных для обработки, необходимо выполнить GET-запрос с<br>
вариантом авторизации Authorization: Bearer и токеном, полученным, при авторизации

```cmd
curl --location 'localhost:8000/api/return_book/<N>' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwiZXhwIjoxNzIyNTAyOTM2fQ.haSeeMybF_TPKtjvA6NC7E-je-Yo0oWlhCZf8HaOMLc' \
--data ''
```
Вместо <N> следует указать ID возвращаемой книги.

Будет получен ответ вида:
 ```cmd
...
{
    "user": {
        "Операция": "Успешно"
    }
}

ИЛИ

{
    "user": {
        "Операция": "Неудача"
    }
}
```

<br>
<h3>Для получения списка должников и книг "на руках" </h3>
* Для отправки данных для обработки, необходимо выполнить GET-запрос с<br>
вариантом авторизации Authorization: Bearer и токеном, полученным, при авторизации

```cmd
curl --location 'localhost:8000/api/books_on_hands' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwiZXhwIjoxNzIyNTAyOTM2fQ.haSeeMybF_TPKtjvA6NC7E-je-Yo0oWlhCZf8HaOMLc' \
--data ''
```

Будет получен ответ вида:
 ```cmd
...
"books_on_hands": [
            {
                "id": 5,
                "book": {
                    "id": 6,
                    "title": "Девушка с татуировкой дракона",
                    "author": "Стиг Ларссон",
                    "genre": "детектив"
                },
                "reader": {
                    "username": "reader1",
                    "email": "reader1@mail.ru",
                    "full_name": "Иван Иванов",
                    "phone": "+16665554444",
                    "address": "Пушкина 15-1"
                },
                "date_taken": "2024-06-29T00:00:00Z",
                "date_since_taked": 32
            },
```




