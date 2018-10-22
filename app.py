from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello():
    names = ("Jacob", "John", "Rob", "Katie", "Becky", "Susan", "Stanley")
    return render_template('index.html', users=names, weather= "Sunny")


@app.route('/about')
def about():
    return render_template('about.html')


app.run()
