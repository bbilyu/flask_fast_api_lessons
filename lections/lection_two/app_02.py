from markupsafe import escape
from flask import Flask, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'

@app.route('/test_url_for/<int:num>/')
def url_test(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("url_test", num=42) = }<br>'
    text += f'Функция {url_for("url_test", num=42,data="new_data") = }<br>'
    text += f'Функция {url_for("url_test", num=42,data="new_data", pi=3.14515) = }<br>'
    return text

if __name__ == '__main__':
    app.run(debug=True)
