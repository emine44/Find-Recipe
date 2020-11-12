"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import requests

import crud
import model
import server

os.system('dropdb recipes')
os.system('createdb recipes')

model.connect_to_db(server.app)
model.db.create_all()



with open('data/cuisine_list.json') as f:
    cuisine_data = json.loads(f.read())
# Create cusines, store them in a list so we can add to dropdown menu
cuisine_list_in_db=[]
for cuisine in cuisine_data:
    cuisine_country=cuisine['cuisine_country']

    db_cuisine=crud.create_cuisine(cuisine_country)
    cuisine_list_in_db.append(db_cuisine)

# Create users, store them in a list so we can add to dropdown menu
with open('data/user_list.json') as u:
    user_data = json.loads(u.read())
    user_list_in_db=[]
for user in user_data:
    user_name, email , password = (user['user_name'],user['email'],user['password'])

    db_user=crud.create_user(user_name,email,password)
    user_list_in_db.append(db_user)

# Create dishes
with open('data/dish_list.json') as d:
    dish_data = json.loads(d.read())
    dish_list_db=[]
for dish in dish_data:
    cuisine_id,dish_id,name,image = (dish['cuisine_id'],dish['id'],dish['title'],dish['image'])

    db_dish=crud.create_dish(cuisine_id,dish_id,name,image)
    dish_list_db.append(db_dish)

# Create ratings
with open('data/rating_list.json') as r:
    rating_data = json.loads(r.read())
    rating_list_db=[]
for rating in rating_data:
    score,dish_id,user_id = (rating['score'],rating['dish_id'],rating['user_id'])

    db_rating=crud.create_rating(score,dish_id,user_id )
    dish_list_db.append(db_rating)



