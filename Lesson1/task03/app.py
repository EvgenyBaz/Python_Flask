# Задание №3
# 📌 Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contacts.html")

@app.route("/add_nums/<int:num/int:num2>")
def add_num(a,b):
    return str(a+b)

if __name__== "__main__":
    app.run()