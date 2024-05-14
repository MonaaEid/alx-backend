#!/usr/bin/env python3
"""instantiate the Babel object in your app."""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return 2-index.html"""
    return render_template('2-index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
