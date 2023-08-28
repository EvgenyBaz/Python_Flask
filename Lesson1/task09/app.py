# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/clo1/')
def clo1():
    return render_template('clo1.html')

@app.route('/clo2/')
def clo2():
    return render_template('clo2.html')

@app.route('/clo3/')
def clo3():
    return render_template('clo3.html')

@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')

@app.route('/jac1/')
def jac1():
    return render_template('jac1.html')

@app.route('/jac2/')
def jac2():
    return render_template('jac2.html')

@app.route('/jac3/')
def jac3():
    return render_template('jac3.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.route('/sho1/')
def sho1():
    return render_template('sho1.html')

@app.route('/sho2/')
def sho2():
    return render_template('sho2.html')

@app.route('/sho3/')
def sho3():
    return render_template('sho3.html')



if __name__ == '__main__':
    app.run()
