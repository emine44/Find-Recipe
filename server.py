"""Server for movie ratings app."""

from flask import Flask, request, flash, session
from flask import render_template, Blueprint, render_template, redirect, url_for
from jinja2 import StrictUndefined
import crud
from model import db, User, Cuisine, Rating, Dish, connect_to_db
from data import get_dish_summary,get_ingredients,get_instructions,get_equipments,get_joke

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# routes and view functions!
@app.route('/')
def display_homepage():
    joke=get_joke()
    return render_template('homepage.html',joke=joke)


@app.route('/login', methods=['GET', 'POST'])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    if crud.validate_user_login(email, password) == 'valid':
        session['current_user'] = email
        flash(f'Logged in as {email}')
        print("*****************************************")
        print("success!!!")
        print("*****************************************")
        return redirect("/cuisine_list")
    else:
        flash("invalid!!!")
        print("*****************************************")
        print("invalid!!!")
        print("*****************************************")
        return redirect("/")


@app.route('/cuisine_list',  methods=['GET', 'POST'])
def all_cuisines():

    user= User.query.filter_by(email = session["current_user"]).one()
    
    cuisine_list = crud.get_all_cuisines()
    dish_list = crud.get_dishes()
    ratings = crud.get_all_ratings()

    return render_template('cuisine_list.html', items=cuisine_list, user=user, dish_list=dish_list,ratings=ratings)



@app.route('/sign_up', methods=['GET', 'POST'])
def display_sign_up():
    return render_template("sign_up.html")


@app.route('/sign_up/register', methods=["POST"])
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    # all_users= crud.get_users()
    
    

    crud.create_user(user_name=username, email=email, password=password)
    
    
    print('*'*20)
    print('/n')
    print(username)
    print('*'*20)

    return render_template("homepage.html")


@app.route('/dish_details', methods=['GET', 'POST'])
def get_dish_details():
    """Show individual dish's info."""
    user_id=session["user_id"]
    score =request.form.get("rate")
    if request.method=='POST': 
        dish_id = request.form.get("dish_id")
    else:
        dish_id = request.args.get("dish_id")
    if score!=None: 
        crud.create_rating(score=score,dish_id=dish_id,user_id=user_id)
        flash("you rated!!!")
   
    

    dish= Dish.query.get(dish_id)
    summary = get_dish_summary(dish_id)
   
    ingredients=get_ingredients(dish_id)
    equipments=get_equipments(dish_id)
    instructions=get_instructions(dish_id)
    
   
    


    print(dish_id)
    print('*'*20)

    print(score)
    print('*'*20)
    
    print('*'*20)

    return render_template('dish_details.html', summary=summary,ingredients=ingredients,equipments=equipments,instructions=instructions,dish=dish,rate=score)


# @app.route('/user_profile')
# def all_users():
#     """View user_details"""

#     return render_template('user_profile.html')

@app.route('/about_project')
def display_about():
    """View project details"""

    return render_template('about.html')

@app.route('/contact_us')
def display_contact():
    """View contact page"""

    return render_template('contact.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
