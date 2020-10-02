from flask import Flask, redirect, url_for



# create app
app = Flask(__name__)


#decorator for each route
@app.route('/')
def home():
    return 'Hello, this is the main page <h1>HELLO<h1>'


@app.route('/<name>')
def user(name):
    return f'hello {name}'



@app.route('/admin')
def admin():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()

