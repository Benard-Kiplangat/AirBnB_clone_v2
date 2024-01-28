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


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
