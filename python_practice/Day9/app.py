from flask import Flask

app=Flask(__name__)

@app.route('/')

def home():
    return "Hello from flask"

@app.route('/about')

def about():
    return "This is my first flask app"

@app.route('/name')

def name():
    return "Hello I'm Kritika"

@app.route('/weather')

def weather():
    return "Weather app comming soon"

@app.route('/calculator')

def calculator():
    return "Calculator comming soon"

@app.route('/shopping')

def shopping():
    return "Shopping cart comming soon"


@app.route('/user/<name>')

def user(name):
    return f"Hello {name}! Welcome to my app!"

if __name__== '__main__':
    app.run(debug=True)