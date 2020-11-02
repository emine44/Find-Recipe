"""Models for movie ratings app."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# Replace this with your code!
class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_name =db.Column(db.String)
    email = db.Column(db.String, unique= True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id= {self.user_id} email={self.email}>'

class Cuisine(db.Model):
    """A movie."""

    __tablename__ = 'cuisines'

    cuisine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cuisine_country = db.Column(db.String)
    dish_id = db.Column(db.Integer)

    def __repr__(self):
        return f'<Cuisine cuisine_id={self.movie_id} cuisine_country={self.cuisine_country}>'  

class Dish(db.Model):
    """A movie."""

    __tablename__ = 'dishes'

    dish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cuisine_id = db.Column(db.String)
    name = db.Column(db.String)
    recipe = db.Column(db.Text)
    name = db.Column(db.String)
    ingredients = db.Column(db.Text)
    image=db.Column(db.String)
    rating_id=db.Column(db.Integer)
    

    def __repr__(self):
        return f'<Cuisine cuisine_id={self.movie_id} cuisine_country={self.cuisine_country}>'  

class Rating(db.Model):
    """A movie rating."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)
    dish_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'  

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = True
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!') 


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
   