from flask import Flask, render_template

app = Flask(__name__)

html = """
<h1>Привет,меня зовут Илья</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
def index():
    return f'Hi!'


@app.route('/users/')
def users():
    _users  = [{'name': 'David',
                 'email': 'david@example.com',
                 'phone': '(345) 567-1010'},
                {'name': 'Michael',
                 'email': 'michael@example.com',
                 'phone': '(234) 789-1234'},
                {'name': 'Emma',
                 'email': 'emma@example.com',
                 'phone': '(678) 456-7890'
                 }, ]
    context = {'users': _users,
               'title': 'Точечная нотация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
