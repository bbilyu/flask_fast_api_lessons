from flask import Flask,render_template

app = Flask(__name__)

html = """
<h1>Привет,меня зовут Илья</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
def index():
    return f'Hi!'


@app.route('/index/')
def html_index():
    context = {
        'title': ['samsung','lg','apple'],
        'name':'Вася',
    }
    return render_template('index.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
