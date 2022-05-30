# Тестовое задание для automation engineer

Тестовое задание состоит из 2х частей, обе части должны быть выполнены на языке
Python 3.7+.
Результаты залить на github или gitlab на ваш выбор.

## Задача 1
Написать api contacts, адресная книга, которая хранит имя, фамилию, email,
телефон и адрес, написать Dockerfile.

Затем покрыть необходимыми тестами. Тесты должны быть вынесены в отдельный проект,
то есть это не unit тесты, а отдельный тестовый фреймворк. В качестве раннера
используем pytest.

Все api будет отдавать данные в формате JSON.

Можно использовать любые фреймворки на ваш выбор flask, django и другие.

Приложение должно иметь следующие api методы:
1. GET /api/contacts - список всех контактов
```JSON
[
  {
    "id": 1,
    "email": "some_email@mail.ru",
    "first_name": "Michael",
    "last_name": "Lawson",
    "phone": "+79680000000",
    "country": "Russia",
    "city": "Moscow",
    "address": "125167, Leningradsky prospekt 39 bld. 79"
  },
  {
  "id": 2,
  "email": "adminl@mail.ru",
  "first_name": "Michael",
  "last_name": "Right",
  "phone": "+79680000001",
  "country": "Russia",
  "city": "Moscow",
  "address": "125167, Leningradsky prospekt 39 bld. 79"
  }
]
```

2. POST /api/contacts - добавление контакта 
   Принимает JSON вида, обязательными полями являются first_name и email:
```JSON
{
  "email": "some_email_3@mail.ru",
  "first_name": "Jake",
  "last_name": "Watson",
  "phone": "+79680000099",
  "country": "United States",
  "city": "New York",
  "address": "125167, Leningradsky prospekt 39 bld. 79"
}
```

3. GET /api/contact/{CONTACT_ID} - просмотр одного контакта
```JSON
{
  "id": 3,
  "email": "some_email@mail.ru",
  "first_name": "Tobias",
  "last_name": "Michael",
  "phone": "+79680000000",
  "country": "Russia",
  "city": "Moscow",
  "address": "125167, Leningradsky prospekt 39 bld. 79"
}
```
4. DELETE /api/contact/{CONTACT_ID} - удаление контакта
4. PUT /api/contact/{CONTACT_ID} - изменение данных контакта
```JSON

{
  "email": "my_awersome_email@mail.ru"
}
```

## Задача 2
Покрыть необходимыми тестами саджесты в поисковой строке по адресу https://go.mail.ru/

Использовать стандартный биндинг для Selenium - https://pypi.python.org/pypi/selenium. В качесте тестраннера использовать pytest - https://docs.pytest.org/en/latest/. 



## Задача 3 (автоматизация не требуется, только тест дизайн)
Одна из задач на проекте - тестирование скиллов Маруси.
Среди таких скиллов есть Напоминания (можно познакомиться в приложении) - мы просим Марусю напомнить нам о чем-то в определенное время; как только наступает момент,
приложение/колонка сигнализируют об имеющемся напоминании и озвучивают его.
Необходимо составить смоук тест для данного скилла.