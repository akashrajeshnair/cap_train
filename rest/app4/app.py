from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello {name}"

#app.add_url_rule('/', 'hello', hello)

if __name__ == '__main__':
    app.run(port=3000, debug=True)