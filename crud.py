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


# ########## RATING ############

def create_rating(score, dish_id, user_id):
    """Create and return a new rating."""

    rating = Rating(score=score, dish_id=dish_id,user_id=user_id)

    db.session.add(rating)
    db.session.commit()

    return rating




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    

    # country_list=[]
    # for i in range(10):
    #     a=seed_database.cuisine_data[i]["cuisine_country"]
    #     country_list.append(a)
    # cuisine_list=[]
    # for u in Cuisine.query.all():
    #     cuisine_list.append(u.__dict__["cuisine_country"])

    # # print(cuisine_list)
    for a in get_dishes():
        print(a.dish_id,a.name)
    

    
     

