#!/usr/bin/python3
"""Index view for API status check."""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def get_status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """Retrieves the number of each object by type"""
    objects = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
