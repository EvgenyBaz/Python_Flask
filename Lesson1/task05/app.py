# Задание №4
# 📌 Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('base.html')

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contacts.html")

@app.route("/add_nums/<int:num/int:num2>")
def add_num(a,b):
    return str(a+b)

@app.route('/str-len/<str_inp>')
def str_len(str_inp):
    return str(len(str_inp))


if __name__== "__main__":
    app.run()