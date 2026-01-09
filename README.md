### Backend-приложение на Django для работы с гео-точками

 
### Описание 
 
### API для работы с гео-точками

**Функционал** 

Реализован API для публикации постов 

Аутентификация по JWT-Токену  

Поддерживает методы GET, POST

Предоставляет данные в формате JSON 

**Установка и как запустить проект**

1. Клонировать репозиторий
   
```git clone https://github.com/Egor-FilonovLol/APIGEO.git```

2. Собрать образ и запустить контейнер.
 
 ```docker-compose up --build```



### SWAGGER-URL
```/swagger/```
### REDOC-URL
```/redoc/```

### API-Эндпоинты

**Получения токена**

---

```POST api/v1/token/```

Тело запроса

```
{
    "username":
        "egor",
    "password": 
        "123"
}
```

**Ответ(201 created)**

```
{
  "refresh": "<ваш_refresh_токен>",
  "access": "<ваш_access_токен>"
}
```

---

**Создать точку на карте**

```POST /api/v1/points/```

**Тело запроса**
```
{
    "name":
        "Name_Token",
    "latitude": 
        "-41.243433",
    "longitude": 
        "-21.432323"
}
```

**Ответ(201 created)**

```
{
    "id": 1,
    "name": "Name_Token",
    "lat": -41.243433,
    "lon": -21.432323,
    "description": ""
}
```

**Создать сообщение к точке**

```POST api/v1/points/1/messages/```

**Тело запроса**

```
{
    "message": 
        "Required_Message_For_Point" 
}
```


**Ответ (201 created)**

```
{
    "id": 1,
    "message": "Required_Message_For_Point",
    "location": {
        "id": 1,
        "name": "Name_Token",
        "lat": -41.243433,
        "lon": -21.432323
    },
    "author": "egor"
}
```

---

**Поиск точки в заданном радиусе**

```GET /api/v1/points/search/?latitude=-40&longitude=-20&radius=200```

**Ответ**

```
[
    {
        "id": 1,
        "name": "Name_Token",
        "lat": -41.243433,
        "lon": -21.432323,
        "description": ""
    }
]
```
---

**Поиск точек в радиусе**

```GET /api/v1/messages/search/?latitude=-39&longitude=-42&radius=1800```

**Ответ**

```
[
    {
        "id": 1,
        "message": "Required_Message_For_Point",
        "location": {
            "id": 1,
            "name": "Name_Token",
            "lat": -41.243433,
            "lon": -21.432323
        },
        "author": "egor"
    }
]
```
------------
