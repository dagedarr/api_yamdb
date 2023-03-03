<img src="logo.png" align="right" />

## Проект YaMDb собирает отзывы пользователей на различные произведения.

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)


## Возможности API: 
- регистрация пользователей 🤷‍♂️
- получение токенов для доступа 🔑
- просмотр, публикация, редактирование, удаление записей ✍️
- комментирование записей 💬
- реализована пагинация 📖

## Установка 🛫

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/vansbass/api_yamdb.git
```
```
cd api_yamdb
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
## Примеры некоторых запросов API 🚀
|Метод   |URL                                            |Описание                               |
|:------:|:----------------------------------------------|:--------------------------------------|
| POST   | /api/v1/auth/signup/                          | Регистрация нового пользователя       |
| POST   | /api/v1/auth/token/                           | Получение JWT-токена                  |
| GET    | /api/v1/users/me/                             | Получение данных своей учетной записи |
| GET    | /api/v1/titles/                               | Получение списка всех произведений    |
| GET    | /api/v1/titles/{title_id}/reviews/            | Получение списка всех отзывов         |

Более подробная документация доступна после запуска проекта по адресу: 📄
> [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)