from flask import Flask,render_template

app = Flask(__name__)

html = """
<h1>Привет,меня зовут Илья</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
def index():
    return f'Hi!'


@app.route('/for/')
def show_for():
    context = {
        'title': 'Ветвление',
        'poems': ['Вот не думал не гадал',
                  'Программистом взял и стал',
                  'Хитрый знает он язык'],
    }
    return render_template('show_for.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
