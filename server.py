"""Server for movie ratings app."""

from flask import Flask, request,flash
from flask import render_template,Blueprint, render_template, redirect, url_for
from jinja2 import StrictUndefined
import crud
from model import db, User, Cuisine, Rating,Dish, connect_to_db

app = Flask(__name__) 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


#routes and view functions!
@app.route('/')
def display_homepage():
    return render_template('homepage.html') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    cuisine_list=crud.get_all_cuisines()
    dish_list=crud.get_dishes()

    email = request.form.get("email")
    password = request.form.get("password")
    user= crud.get_user_by_email(email)
    if crud.validate_user_login(email,password)=='valid':
        # session['current_user'] = email
        # flash(f'Logged in as {email}')
        flash("success!!!")
        print("*****************************************")
        print("success!!!")
        print("*****************************************")
        return render_template('cuisine_list.html',items=cuisine_list, user=email,dish_list=dish_list) 
    else:
        flash("invalid!!!")
        print("*****************************************")
        print("invalid!!!")
        print("*****************************************")
        return redirect("/")

@app.route('/cuisine_list',  methods=['GET', 'POST'])
def all_cuisines():
    return render_template('cuisine_list.html')

@app.route('/sign_up',methods=['GET','POST'])
def display_sign_up():
    return render_template("sign_up.html")

@app.route('/sign_up/register', methods=["POST"])
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    username =request.form.get('username')
    # all_users= crud.get_users()
    crud.create_user(user_name=username,email=email, password=password)
    print('*'*20)
    print('/n')
    print(username)
    print('*'*20)
    return render_template("homepage.html")

    


# @app.route('/user_profile')
# def all_users():
#     """View user_details"""

#     return render_template('user_profile.html')


# @app.route('/dish_details')
# def all_users():
#     """View all users."""

#     return render_template('dish_details.html')    

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
