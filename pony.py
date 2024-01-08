import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

# Пишем свой API-key из https://derpibooru.org/registrations/edit
api_key = "nYTuAw8EHfHyfL6TgXPk"

# Ищем картинки на derpi
def get_random_batpony_image():
    url = f"https://derpibooru.org/api/v1/json/search?q=batpony%2Csafe&key={api_key}"
    response = requests.get(url)
    data = response.json()

    images = data["images"]
    random_image = random.choice(images)

    return {
        "image_url": random_image["representations"]["full"],
        "view_url": random_image["view_url"],
        "tags": random_image["tags"]
    }
#Обрабатываем маршрут
@app.route("/")
def index():
    random_batpony_image = get_random_batpony_image()
    return render_template("index.html", image_url=random_batpony_image["image_url"],
                           view_url=random_batpony_image["view_url"],
                           tags=random_batpony_image["tags"])

if __name__ == "__main__":
    app.run(debug=True)