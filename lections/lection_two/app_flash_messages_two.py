from flask import Flask, flash, redirect, render_template,request, url_for

app = Flask(__name__)
app.secret_key = b'e02760316934f88950fc2e18e96d2da5a4f70ec2eeeec5b6dcd6ee9f7ac4ad08'

# Простейший способ генерации такого ключа, выполнить следующие пару строк
# кода
# >>> import secrets
# >>> secrets.token_hex()


@app.route('/')
def index():
    return 'Hi'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)