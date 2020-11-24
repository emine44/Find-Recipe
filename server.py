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

    cuisine_list = crud.get_all_cuisines()
    dish_list = crud.get_dishes()
    ratings = crud.get_all_ratings()


    
    
    # total = sum(r.score for r in ratings_list)
    # avg_rating = float(total / len(ratings_list))

   




    email = request.form.get("email")
    password = request.form.get("password")

    user= User.query.filter_by(email = request.form["email"]).one()
    




    if crud.validate_user_login(email, password) == 'valid':
        # session['current_user'] = email
        # flash(f'Logged in as {email}')
        flash("success!!!")
        print("*****************************************")
        print("success!!!")
        print("*****************************************")
        return render_template('cuisine_list.html', items=cuisine_list, user=user, dish_list=dish_list,ratings=ratings)
    else:
        flash("invalid!!!")
        print("*****************************************")
        print("invalid!!!")
        print("*****************************************")
        return redirect("/")


@app.route('/cuisine_list',  methods=['GET', 'POST'])
def all_cuisines():
    return render_template('cuisine_list.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def display_sign_up():
    return render_template("sign_up.html")


@app.route('/sign_up/register', methods=["POST"])
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')
    # all_users= crud.get_users()
    
    

    user= crud.create_user(user_name=username, email=email, password=password)

    session['user_id']=user.user_id
    print('*'*20)
    print('/n')
    print(username)
    print('*'*20)

    session['score']=request.args.get('score')
    return render_template("homepage.html")


@app.route('/dish_details', methods=['GET', 'POST'])
def get_dish_details():
    """Show individual dish's info."""

    dish_id = request.args.get("dish_id")
    dish= Dish.query.get(dish_id)
    summary = get_dish_summary(dish_id)
    ingredients=get_ingredients(dish_id)
    equipments=get_equipments(dish_id)
    instructions=get_instructions(dish_id)
    
    # crud.create_rating(score,dish_id,session['user_id'])
        


    print(dish_id)
    print('*'*20)
    
    
    print('*'*20)

    return render_template('dish_details.html', summary=summary,ingredients=ingredients,equipments=equipments,instructions=instructions,dish=dish)


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
