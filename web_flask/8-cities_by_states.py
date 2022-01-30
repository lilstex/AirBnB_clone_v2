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


@app.route('/cities_by_states', strict_slashes=False)
def citieslist():
    """This function will send all the states in the storage
    to the template"""
    cities = storage.all(City).values()
    states = storage.all(State).values()
    cities = sorted(cities, key=lambda cities: cities.name)
    states = sorted(states, key=lambda states: states.name)

    return render_template('8-cities_by_states.html', stateobj=states,
                           cityobj=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)