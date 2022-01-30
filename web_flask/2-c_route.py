#!/usr/bin/python3
"""
This python script will start a flask web app
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """This function will print a line whenever it is no the root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function will print HBNB when it is on a specific route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_isfun(text):
    """This function will print the name to whatever
    is in the specific route followerd by C"""
    name = text.replace("_", " ")
    return "C {}".format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)