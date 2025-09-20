from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuario de prueba (en un sistema real se usaría una base de datos)
USUARIO = {
    "username": "admin",
    "password": "12345"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USUARIO['username'] and password == USUARIO['password']:
        return redirect(url_for('welcome', user=username))
    else:
        return render_template('login.html', error="Usuario o contraseña incorrectos.")

@app.route('/welcome/<user>')
def welcome(user):
    return render_template('welcome.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
