from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resp = make_response(redirect('/welcome'))
        resp.set_cookie('name', name)
        resp.set_cookie('email', email)
        return resp

    return render_template('index.html')

@app.route('/welcome')
def welcome():
    if 'name' in request.cookies and 'email' in request.cookies:
        name = request.cookies['name']
        return render_template('welcome.html', name=name)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run()