from flask import Flask,render_template

app = Flask(__name__)

html = """
<h1>Привет,меня зовут Илья</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
def index():
    return f'Hi!'


@app.route('/if/')
def show_if():
    context = {
        'title': 'Ветвление',
        'user':'Крутой хакер',
        'number':1,
    }
    return render_template('show_if.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
