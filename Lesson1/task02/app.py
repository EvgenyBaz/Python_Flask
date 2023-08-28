# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Добавьте две дополнительные страницы в ваше веб-
# приложение:
# ○ страницу "about"
# ○ страницу "contact".

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/about")
def about():
    return render_template("/about.html/")

@app.route("/contact")
def contact():
    return render_template("/contacts.html/")

if __name__== "__main__":
    app.run()