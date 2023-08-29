# UsersController.py

from models.UserModel import User
from models.schema.UserSchema import user_schema, users_schema
from flask import abort, make_response
from config import db
from werkzeug.security import generate_password_hash

# Create User
def create(user):
    fname, lname, email, password = user.get('fname'), user.get('lname'), user.get('email'), user.get('password')
    existing_person = User.query.filter(User.email == email).one_or_none()

    if existing_person is None:
        # new_user = user_schema.load(user, session=db.session)
        new_user = User(fname = fname,lname = lname,email = email,password = generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"User with email {email} already exists")

# Read User
def read_one(email):
    user = User.query.filter(User.email == email).one_or_none()
    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"User with email {email} not found")

# Update User
def update(email, user):
    existing_user = User.query.filter(User.email == email).one_or_none()
    if existing_user:
        existing_user.fname = user["fname"]
        existing_user.lname = user["lname"]
        existing_user.email = user["email"]
        existing_user.password = user["password"]
        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201
    else:
        abort(404, f"User with email {email} not found")

# Delete User
def delete(email):
    existing_user = User.query.filter(User.email == email).one_or_none()
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"User with email {email} successfully deleted", 200)
    else:
        abort(404, f"User with email {email} not found")

# Read all Users
def read_all():
    # return "hey"
    users = User.query.all()
    return users_schema.dump(users)