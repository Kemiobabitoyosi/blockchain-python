#!/usr/bin/python3
import pathlib
from api.views import api_views
from flask import (
    Flask,
    make_response,
    jsonify
)


# initialize flask app
app = Flask(__name__)
# register/mount blueprint
app.register_blueprint(api_views)
# allow missing trailing
app.url_map.strict_slashes = False


@app.errorhandler(404)
def not_found(error):
    """
    Handle non existing objects

    Args:
    error: [description]

    Returns:
    JSON: json object
    """

    e = {
        "error": "Not Found"
    }
    return make_response(jsonify(e), 404)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = "5555"
    app.run(host=host, port=port)
