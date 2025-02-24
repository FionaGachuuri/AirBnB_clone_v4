#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template
from models import storage
import uuid

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False

HOST = '0.0.0.0'
PORT = 5000


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    Close the database session after each request
    """
    storage.close()


@app.route('/1-hbnb/')
def hbnb_filters():
    """
    Renders the 1-hbnb.html template with states, cities, amenities, places, and users
    """

    # Fetching all states and organizing them in a dictionary sorted by name
    state_dict = {state.name: state for state in storage.all(State).values()}

    # Fetching all amenities, places, and users
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all(User).values()}

    # Generating a unique cache ID to prevent caching issues
    cache_id = str(uuid.uuid4())

    return render_template(
        '1-hbnb.html',
        states=state_dict,
        amens=amenities,
        places=places,
        users=users,
        cache_id=cache_id
    )


if __name__ == "__main__":
    """
    Start the Flask application
    """
    app.run(host=HOST, port=PORT, debug=True)

