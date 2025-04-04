from flask import Flask, render_template
import os

app = Flask(__name__)

# Список изображений для галереи
def get_images():
    image_folder = os.path.join('static', 'images')
    images = []
    for f in os.listdir(image_folder):
        if f.lower().endswith(('.jpg', '.png', '.jpeg')):
            # Формируем правильный путь
            images.append(f"images/{f}")
            print(f"Добавлено изображение: images/{f}")  # Для отладки
    return images

# Главная страница с вкладками
@app.route('/')
def index():
    images = get_images()
    tabs = [
        {'id': 'home', 'title': 'Главная', 'content': 'Добро пожаловать на наш сайт!'},
        {'id': 'gallery', 'title': 'Галерея', 'content': images},
        {'id': 'about', 'title': 'О нас', 'content': 'Мы нефига не делаем страдаем фигней.'},
        {'id': 'contact', 'title': 'Контакты', 'content': 'А зачем вам наши контакты?.'}
    ]
    return render_template('index.html', tabs=tabs)

if __name__ == '__main__':
    app.run(debug=True)