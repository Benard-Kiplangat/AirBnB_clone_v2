#!/usr/bin/python3
"""
Prints Hello, HBNB! on route "/", HBNB on route "/hbnb", and
C is + text variable passed to route
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """Returns Hello, HBNB!"""
    return "Hello, HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<string:cvariable>', strict_slashes=False)
def c_route(cvariable):
    """Returns C is + text passed"""
    cvariable = cvariable.replace("_", " ")
    return "C is %s" % cvariable


if __name__ == "__main__":
    app.run(host="0.0.0.0")
