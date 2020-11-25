"""CRUD operations."""
import json
from model import db, User, Cuisine, Rating,Dish, connect_to_db
from flask import Flask
import json

# ########## USER ############

def create_user(user_name,email, password):
    """Create and return a new user."""

    user = User(user_name=user_name,email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).all()

def validate_user_login(email,password):
    user=User.query.filter(User.email==email and User.password==password).first()
    if user!=None:
        return "valid"
    else:
        return "invalid"

# ########## CUISINE ############

def create_cuisine(cuisine_country):
    """Create and return a new user."""

    cuisine = Cuisine(cuisine_country=cuisine_country)

    db.session.add(cuisine)
    db.session.commit()

    return cuisine

def get_cuisine_by_id(cuisine_id):
    """Return a movie by primary key."""

    return Cuisine.query.get(cuisine_id)

def get_all_cuisines():
    # cuisine_list=[]
    # for u in Cuisine.query.all():
    #     cuisine_list.append(u.__dict__["cuisine_country"])
    # return cuisine_list
    return Cuisine.query.all()


# ########## DISH ############

def create_dish(cuisine_id,dish_id,name,image):
    """Create and return a new movie."""

    dish = Dish(cuisine_id=cuisine_id,
                dish_id=dish_id,
                name=name,
                image=image)
                 

    db.session.add(dish)
    db.session.commit()

    return dish


def get_dishes():
    """Return all movies."""

    return Dish.query.all()

def get_dish_by_cuisine_id(cuisine_id):
    
    dish_list=[]
    for u in Dish.query.filter(Dish.cuisine_id== cuisine_id).all():
        dish_list.append(u)
    return dish_list

def get_dish_by_id(dish_id):
    dish=Dish.query.filter(Dish.dish_id==dish_id).all()
    return dish


# ########## RATING ############

def create_rating(score, dish_id, user_id):
    """Create and return a new rating."""

    rating = Rating(score=score, dish_id=dish_id,user_id=user_id)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_all_ratings():
    rating=Rating.query.all()
    return rating

# count=SELECT count(Rating.score) FROM Where Rating.dish_id=''
def get_average_rating(dish_id):
    count=Rating.query(Rating.score.count()).filter(Rating.dish_id==dish_id)
    return count
# length=SELECT SUM(Rating.score) FROM Where Rating.dish_id=''
def get_length_rating(dish_id):
    length=Rating.query(sum(Rating.score)).filter(Rating.dish_id==dish_id)            
    return length

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    

    # rating_list=[]
    # for rating in get_all_ratings():
    #     rating_list.append(rating)
    # # print (rating_list)
    
    # total=0
    # count=0
    # for r in rating_list:
    #     if r.dish_id==644488:
    #        total=total + r.score
    #        count=count+1
    # print (float(total/count))
   

    
