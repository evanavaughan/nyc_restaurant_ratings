from flask import render_template
from dash_package import server, app


@server.route('/nyc_restaurants')
def render_restaurants():
    return "Hello world"
