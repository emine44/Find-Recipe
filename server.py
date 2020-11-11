"""Server for movie ratings app."""

from flask import Flask, request
from flask import render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#routes and view functions!
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/cuisine_list', methods=['POST'])
def all_cuisines():
    """View all cuisines."""
    items=["African","German","Mexican","Korean","Indian"]
    name= request.form.get("email")

    return render_template('cuisine_list.html',items=items,name=name)

@app.route('/sign_up')
def signUp():

    return render_template('sign_up.html')


# @app.route('/user_profile')
# def all_users():
#     """View user_details"""

#     return render_template('user_profile.html')


# @app.route('/dish_details')
# def all_users():
#     """View all users."""

#     return render_template('dish_details.html')    

if __name__ == '__main__':
    # connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
