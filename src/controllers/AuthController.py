# AuthController.py

from flask import request, abort, jsonify, abort, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from models.UserModel import User
from config import app, db
from models.schema.UserSchema import user_schema

# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps

# decorator for verifying the JWT
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		# jwt is passed in the request header
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		# return 401 if token is not passed
		if not token:
			return jsonify({'message' : 'Token is missing !!'}), 401

		try:
			# decoding the payload to fetch the stored details
			data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
			current_user = User.query\
				.filter_by(id = data['id'])\
				.first()
		except:
			return jsonify({
				'message' : 'Token is invalid !!'
			}), 401
		# returns the current logged in users context to the routes
		return f(current_user, *args, **kwargs)

	return decorated

# Decode Token
def decodeToken(token):
    try:
        return jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    except:
	    print(jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256']))
	    # abort(401, f"Unauthoirzed123")

# Login 
def login(data):
	email, password = data.get('email'), data.get('password')
	if not data or not email or not password:
		# returns 401 if any email or / and password is missing
		abort(401, f"Missing requried parameters")
		
	user = User.query.filter(User.email == email).one_or_none()

	if not user:
		# returns 401 if user does not exist
		abort(401, f"Incorrect login details")

	if check_password_hash(user.password, password):
		# generates the JWT Token
		token = jwt.encode({
			'id': user.id,
			'exp' : datetime.utcnow() + timedelta(minutes = 60)
		}, app.config['JWT_SECRET_KEY'])

		return make_response(jsonify({'token' : token.decode("utf-8")}), 201)
	# returns 403 if password is wrong
	abort(403, f"Invalid password")

# Register 
def register(data):
	fname, lname, email, password = data.get('fname'), data.get('lname'), data.get('email'), data.get('password')
	if not data or not fname or not lname or not email or not password:
		# returns 401 if any field is missing
		abort(401, f"Missing requried parameters")
		
	user = User.query.filter(User.email == email).one_or_none()

	if user is None:
		new_user = User(fname = fname,lname = lname,email = email,password = generate_password_hash(password))
		db.session.add(new_user)
		db.session.commit()
		return user_schema.dump(new_user), 201
	else:
		abort(406, f"User with email {email} already exists")