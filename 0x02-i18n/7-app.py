#!/usr/bin/env python3
"""
Module emulates a user login system
"""
from typing import Union
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Defines a class with a LANGUAGES class attribute equal to ["en", "fr"]
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("7-app.Config")


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """
    returns a html template that prints
    `Welcome to Holberton` as a title
    and `Hello world`as a header
    """
    return render_template("7-index.html")


@babel.localeselector
def get_locale():
    """
    Check if the incoming request contains locale argument
    ----
    if value is a supported locale, return it.
    If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    if "locale" in request.args:
        if request.args["locale"] in app.config["LANGUAGES"]:
            return request.args["locale"]
    elif (
        g.user
        and g.user.get("locale")
        and g.user.get("locale") in app.config["LANGUAGES"]
    ):
        return g.user.get("locale")
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[dict, None]:
    """
    returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed.
    """
    if "login_as" in request.args:
        user_id = int(request.args["login_as"])
        user_dict = users.get(user_id)

        if user_dict:
            return user_dict
    return None


@app.before_request
def before_request() -> None:
    """
    uses get_user to find a user if any,
    and set it as a global on flask.g.user.
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """
    returns a timezone
    ---
    Gets timezone parameter in URL parameters or from user settings
    validate that it is a valid time zone
    """
    user_timezone = request.args.get("timezone", None)
    if not user_timezone and g.user:
        user_timezone = g.user.get("timezone")

    if user_timezone:
        try:
            return pytz.timezone(user_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
