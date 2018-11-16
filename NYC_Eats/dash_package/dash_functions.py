from sqlalchemy import create_engine, func
from __init__ import db
from db_models import Restaurant, TripAdvisor, Infatuation
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine('sqlite:///nyc_restaurants.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def inf_price_rating_hist():
    return db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 3).all()

def rating_comparison(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = db.session.query(Restaurant.name, Infatuation.rating, TripAdvisor.rating).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[1]/2 for i in q], 'y':[i[2] for i in q]}

def rating_price_inf(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = db.session.query(Restaurant.name, Infatuation.price, Infatuation.rating).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[1] for i in q], 'y':[i[2]/2 for i in q]}

def rating_price_ta(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = db.session.query(Restaurant.name, TripAdvisor.rating, TripAdvisor.price).join(TripAdvisor).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[2] for i in q], 'y':[i[1] for i in q]}
