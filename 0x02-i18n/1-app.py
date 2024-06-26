#!/usr/bin/env python3
"""instantiate the Babel object in your app.
Store it in a module-level variable named babel"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Return 0-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
