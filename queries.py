'''
#from models import *
from sqlalchemy import create_engine
#from math import ceil


engine = create_engine('sqlite:///nyc_restaurants.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_neighborhood_restaurants(neighborhood = 'Upper East Side'):
    name_list = []
    object_list = session.query(Restaurant).join(Neighborhood).filter(Neighborhood.name == neighborhood).all()
    for i in object_list:
        name_list.append(i.name)
    return name_list

def avg_price_neighborhood(neighborhood = 'Upper East Side'):
    name_list = []
    object_list = session.query()

def ta_rating_avg_by_neighborhood():
    query_list = session.query(Neighborhood.name, func.avg(TripAdvisor.rating)).join(Restaurant).join(TripAdvisor).group_by(Neighborhood.name).order_by(func.avg(TripAdvisor.rating)).all()
    new_list = []
    for i in query_list:
        (x, y) = i
        y = round(y, 3)
        i = (x, y)
        new_list.append(i)
    return new_list

def rating_box_whisker(neighborhood):
    return session.query(Restaurant.name, TripAdvisor.rating, Infatuation.rating).join(TripAdvisor).join(Infatuation).join(Neighborhood).filter(Neighborhood.name == neighborhood).all()

def get_name_address():
    return session.query(Restaurant.name, Restaurant.address).join(TripAdvisor).all()
    '''
