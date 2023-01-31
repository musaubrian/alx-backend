#!/usr/bin/env python3
"""Instantiates the Babel object in your app"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Defines a class with a LANGUAGES class attribute equal to ["en", "fr"]
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    returns a html template that prints
    `Welcome to Holberton` as a title
    and `Hello world`as a header
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """
    best_match = request.accept_languages.best_match(app.config["LANGUAGES"])
    return best_match


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
