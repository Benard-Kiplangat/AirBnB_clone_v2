#!/usr/bin/python3
"""
Prints hello, HBNB! on route "/" and HBNB on route "/hbnb"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello, HBNB!"""
    return "Hello, HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Returns, HBNB!"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
