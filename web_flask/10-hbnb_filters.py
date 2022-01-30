#!/usr/bin/python3
"""
This python script will start a flask web app
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def sesclose(self):
    """docs"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def Airbnb():
    """This function will send all the states in the storage
    to the template"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    states = sorted(states, key=lambda states: states.name)
    amenities = sorted(amenities, key=lambda amenities: amenities.name)

    return render_template('10-hbnb_filters.html', stateobj=states,
                           amenityobj=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)