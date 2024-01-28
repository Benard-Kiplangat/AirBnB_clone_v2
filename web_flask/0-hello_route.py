#!/usr/bin/python3
"""
Returns Hello, HBNB! on route "/"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Returns Hello, HBNB!"""
    return "Hello, HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
