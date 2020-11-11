"""CRUD operations."""

from model import db, User, Cuisine, Rating,Dish, connect_to_db


def create_user(user_name,email, password):
    """Create and return a new user."""

    user = User(user_name=user_name,email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user
def create_cuisine(cuisine_country):
    """Create and return a new user."""

    cuisine = Cuisine(cuisine_country=cuisine_country)

    db.session.add(cuisine)
    db.session.commit()

    return cuisine


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_dish(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    dish = Dish(title=title,
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)

    db.session.add(dish)
    db.session.commit()

    return dish


def get_dishes():
    """Return all movies."""

    return Dish.query.all()


def get_cuisine_by_id(cuisine_id):
    """Return a movie by primary key."""

    return Cuisine.query.get(cuisine_id)


def create_rating(user, dish, score):
    """Create and return a new rating."""

    rating = Rating(user=user, dish=dish, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
