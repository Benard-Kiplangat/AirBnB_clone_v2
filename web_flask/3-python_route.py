#!/usr/bin/python3
"""
Prints hello, HBNB! on route "/", HBNB on route "/hbnb",
C is + text passed, and Python + text passed or is cool
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


@app.route('/python', strict_slashes=False)
@app.route("/python/<string:pvariable>", strict_slashes=False)
def hbnb_p_route(pvariable="is cool"):
    """Returns Python + text passed or is cool"""
    return "Python {}".format(pvariable.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
