from flask import Flask, redirect, url_for, render_template



# create app
app = Flask(__name__)


#decorator for each route
@app.route('/<name>')
def home(name):
    return render_template('index_with_py.html', content=name, r=2)


@app.route('/<name>')
def user(name):
    return f'hello {name}'



@app.route('/admin')
def admin():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()




