#!/usr/bin/env python3
"""Welcome to Holberton"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """Return 0-index.html"""
    return render_template('0-index.html')
