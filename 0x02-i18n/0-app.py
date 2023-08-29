#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """This function defines the index/root route of the application"""
    return reder_template('0-index.html')


if __name__ == '__main__':
    app.run()
