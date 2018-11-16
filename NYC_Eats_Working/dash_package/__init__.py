from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///nyc_restaurants.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

db = SQLAlchemy(server)
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/', external_stylesheets=external_stylesheets)

# from db_models import Restaurant, Cuisine, Neighborhood, TripAdvisor, Infatuation, Michelin
from db_models import *
from routes import *
from dashboard import *
# from dash_package.db_seed import *
