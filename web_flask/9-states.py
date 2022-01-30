#!/usr/bin/python3
"""
This python script will start a flask web app
"""

from models import storage
from models.state import State
from models.city import City
from collections import OrderedDict
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def sesclose(self):
    """docs"""
    storage.close()


@app.route('/states/', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def stateonly(id):
    """This function will send all the states in the storage
    to the template"""
    cities = storage.all(City).values()
    states = storage.all(State).values()
    cities = sorted(cities, key=lambda cities: cities.name)
    states = sorted(states, key=lambda states: states.name)
    result = '7-states_list.html'
    existance = 0
    if id:
        for n in states:
            if n.id == id:
                existance = 1
        result = '9-states.html'
    if existance == 0:
        id = None
    return render_template(result, stateobj=states,
                           cityobj=cities, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)