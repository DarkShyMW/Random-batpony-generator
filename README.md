# Random-batpony-generator
Ищет картинки и случайно выводит их на главной странице.

## Как установить?

```
git clone https://github.com/DarkShyMW/Random-batpony-generator.git
```

Для начала регистрируемся на https://derpibooru.org/

После всей процедуры регистрации открываем https://derpibooru.org/registrations/edit

От туда копируем ваш api_key. Его вставляем в 8 строку - api_key = "тут_ваш_ключ"

```
pip3 install Flask
pip3 install requests

cd /путь_до_папки/
python3 pony.git

в браузере открываем по адресу:
http://localhost:5000
```

## Как это происходит?

Происходит запрос на https://derpibooru.org, после чего происходит обработка JSon, которое мы получаем в ответ, так как задаем параметры.
Вытаскиваем "image_url", "view_url","tags".
Обрабатываем, что image_url = картинка, view_url = ссылка на картинку, tags = теги картинки.

После всего этого обрабатываем маршрути выдаем на / - нашу картинку.

[![Python application](https://github.com/DarkShyMW/Random-batpony-generator/actions/workflows/python-app.yml/badge.svg)](https://github.com/DarkShyMW/Random-batpony-generator/actions/workflows/python-app.yml)
