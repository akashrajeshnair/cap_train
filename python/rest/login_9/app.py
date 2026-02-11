from flask import Flask, request, flash, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return 'hello'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid username or password'
        else:
            flash('Logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(port=3000, debug=True)