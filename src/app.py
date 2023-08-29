# app.py

from flask import render_template
import config
from config import app, db
from models.UserModel import User
import socket

# from routes.notes_bp import notes_bp
# from routes.users_bp import users_bp
# from routes.auth_bp import auth_bp

# app.register_blueprint(users_bp, url_prefix='/users')
# app.register_blueprint(notes_bp, url_prefix='/notes')
# app.register_blueprint(auth_bp, url_prefix='/auth')

# Create database schema
# with app.app_context():
#     db.drop_all()
#     db.create_all()

app = config.connex_app
app.add_api(config.basedir / "swagger.json")

# @app.route("/")
# def home():
#     users = User.query.all()
#     return render_template("home.html", users=users)


@app.route("/")
def index():
    host = socket.gethostbyname(socket.gethostbyname('infogiants.com'))
    return render_template("index.html", host=host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)