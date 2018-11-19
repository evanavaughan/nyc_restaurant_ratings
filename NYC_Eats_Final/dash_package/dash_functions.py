from sqlalchemy import create_engine, func, or_
from __init__ import db
from db_models import Restaurant, TripAdvisor, Infatuation, Neighborhood
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine('sqlite:///nyc_restaurants.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def ta_price_by_neighborhood():
    one = db.session.query(Neighborhood.name,func.count(Restaurant.name)).join(Restaurant).join(TripAdvisor).filter(TripAdvisor.price == '$').group_by(Neighborhood.name).all()
    two_three = db.session.query(Neighborhood.name,func.count(Restaurant.name)).join(Restaurant).join(TripAdvisor).filter(TripAdvisor.price == '$$ - $$$').group_by(Neighborhood.name).all()
    four = db.session.query(Neighborhood.name,func.count(Restaurant.name)).join(Restaurant).join(TripAdvisor).filter(TripAdvisor.price == '$$$$').group_by(Neighborhood.name).all()
    return [one, two_three, four]

def inf_price_by_neighborhood():
    one = db.session.query(Neighborhood.name,func.count(Restaurant.name)).join(Restaurant).join(Infatuation).filter(Infatuation.price == '$').group_by(Neighborhood.name).all()
    two_three = db.session.query(Neighborhood.name,func.count(Restaurant.name)).join(Restaurant).join(Infatuation).filter(or_(Infatuation.price == '$$', Infatuation.price == '$$$')).group_by(Neighborhood.name).all()
    four = db.session.query(Neighborhood.name,func.count(Restaurant.name)).join(Restaurant).join(Infatuation).filter(Infatuation.price == '$$$$').group_by(Neighborhood.name).all()
    return [one, two_three, four]

def inf_price_rating_hist_1():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$').all()[0][0]
    greater_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_price_rating_hist_2():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$$').all()[0][0]
    greater_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_price_rating_hist_3():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$$$').all()[0][0]
    greater_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_price_rating_hist_4():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$$$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$$$$').all()[0][0]
    greater_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$$$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def ta_price_rating_hist_1():
    less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$').all()[0][0]
    greater_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def ta_price_rating_hist_2():
    less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$$ - $$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$$ - $$$').all()[0][0]
    greater_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$$ - $$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def ta_price_rating_hist_4():
    less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$$$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$$$$').all()[0][0]
    greater_four =  db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$$$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_rating(neighborhood):
    rating_list = []
    for i in db.session.query(Infatuation.rating).join(Restaurant).join(Neighborhood).filter(Neighborhood.name == neighborhood).all():
        rating_list.append(i[0])
    return rating_list

def ta_rating(neighborhood):
    rating_list = []
    for i in db.session.query(TripAdvisor.rating).join(Restaurant).join(Neighborhood).filter(Neighborhood.name == neighborhood).all():
        rating_list.append(i[0])
    return rating_list

def map_data():
    map_list = []
    for i in db.session.query(Restaurant.name, Restaurant.latitude, Restaurant.longitude, TripAdvisor.price, TripAdvisor.rating).join(TripAdvisor).filter(Restaurant.latitude != ' ').all():
        map_list.append(i)
    return map_list
