from sqlalchemy import create_engine, func, or_
from __init__ import db
from db_models import Restaurant, TripAdvisor, Infatuation, Cuisine, Neighborhood
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

engine = create_engine('sqlite:///nyc_restaurants.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def inf_price_by_cuisine():
    one = db.session.query(Cuisine.name,func.count(Restaurant.name)).join(Restaurant).join(Infatuation).filter(Infatuation.price == '$').group_by(Cuisine.name).all()
    two_three = db.session.query(Cuisine.name,func.count(Restaurant.name)).join(Restaurant).join(Infatuation).filter(or_(Infatuation.price == '$$', Infatuation.price == '$$$')).group_by(Cuisine.name).all()
    four = db.session.query(Cuisine.name,func.count(Restaurant.name)).join(Restaurant).join(Infatuation).filter(Infatuation.price == '$$$$').group_by(Cuisine.name).all()
    return [one, two_three, four]

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
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_price_rating_hist_2():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$$').all()[0][0]
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_price_rating_hist_3():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$$$').all()[0][0]
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def inf_price_rating_hist_4():
    less_two = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating < 2).filter(Infatuation.price == '$$$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 2).filter(Infatuation.rating < 4).filter(Infatuation.price == '$$$$').all()[0][0]
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(Infatuation).filter(Infatuation.rating >= 4).filter(Infatuation.price == '$$$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def ta_price_rating_hist_1():
    less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$').all()[0][0]
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def ta_price_rating_hist_2():
    less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$$ - $$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$$ - $$$').all()[0][0]
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$$ - $$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

# def ta_price_rating_hist_3():
#     less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$$$').all()[0][0]
#     two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$$$').all()[0][0]
#     greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$$$').all()[0][0]
#     return [less_two, two_to_four, greater_four]

def ta_price_rating_hist_4():
    less_two = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating < 4.25).filter(TripAdvisor.price == '$$$$').all()[0][0]
    two_to_four = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.25).filter(TripAdvisor.rating < 4.75).filter(TripAdvisor.price == '$$$$').all()[0][0]
    greater_four = one_to_three = db.session.query(func.count(Restaurant.name)).join(TripAdvisor).filter(TripAdvisor.rating >= 4.75).filter(TripAdvisor.price == '$$$$').all()[0][0]
    return [less_two, two_to_four, greater_four]

def rating_comparison(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = db.session.query(Restaurant.name, Infatuation.rating, TripAdvisor.rating).join(TripAdvisor).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[1]/2 for i in q], 'y':[i[2] for i in q]}

def rating_price_inf(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = db.session.query(Restaurant.name, Infatuation.price, Infatuation.rating).join(Infatuation).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[1] for i in q], 'y':[i[2]/2 for i in q]}

def rating_price_ta(): #restaurant name, mich stars, trip advisor rating, infatuation rating
    q = db.session.query(Restaurant.name, TripAdvisor.rating, TripAdvisor.price).join(TripAdvisor).group_by(Restaurant.name).order_by(Restaurant.name).all()
    return {'text': [i[0] for i in q], 'x':[i[2] for i in q], 'y':[i[1] for i in q]}
