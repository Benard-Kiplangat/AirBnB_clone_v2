#!/usr/bin/python3
"""
Prints Hello, HBNB! on route "/", HBNB on route "/hbnb", and
C is + text variable passed to route
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello, HBNB!"""
    return "Hello, HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<string:cvariable>", strict_slashes=False)
def hbnb_c_route(cvariable):
    """Returns C is + text passed"""
    return "C is {}".format(cvariable.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
