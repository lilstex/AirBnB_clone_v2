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
def C_isfun(name):
    """This function will print the name to whatever
    is in the specific route followerd by C"""
    name = name.replace("_", " ")
    return "c {}".format(name)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Py_isfun(text):
    """his function will print the name to whatever
    is in the specific route if theres any followed by python"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isnum(n):
    """This function will print if the route is a number"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)