#!/usr/bin/env python3
"""Sets up a basic flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """
    returns a html template that prints
    `Welcome to Holberton` as a title
    and `Hello world`as a header
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
