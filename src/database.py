# database.py

from datetime import datetime
from config import app, db
from models.UserModel import User, Note
from werkzeug.security import generate_password_hash

USER_NOTES = [
    {
        "fname": "Fairy",
        "lname": "Tooth",
        "email": "fairytooth@mailinator.com",
        "password": generate_password_hash("123456"),
        "notes": [
            ("I brush my teeth after each meal.", "2022-01-06 17:10:24"),
            ("The other day a friend said, I have big teeth.", "2022-03-05 22:17:54"),
            ("Do you pay per gram?", "2022-03-05 22:18:10"),
        ],
    },
    {
        "fname": "Ruprecht",
        "lname": "Knecht",
        "email": "ruprechtknecht@mailinator.com",
        "password": generate_password_hash("123456"),
        "notes": [
            ("I swear, I'll do better this year.", "2022-01-01 09:15:03"),
            ("Really! Only good deeds from now on!", "2022-02-06 13:09:21"),
        ],
    },
    {
        "fname": "Bunny",
        "lname": "Easte",
        "email": "Bunnyeaste@mailinator.com",
        "password": generate_password_hash("123456"),
        "notes": [
            ("Please keep the current inflation rate in mind!", "2022-01-07 22:47:54"),
            ("No need to hide the eggs this time.", "2022-04-06 13:03:17"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in USER_NOTES:
        new_user = User(
            fname=data.get("fname"),
            lname=data.get("lname"),
            email=data.get("email"),
            password=data.get("password")
        )
        for content, timestamp in data.get("notes", []):
            new_user.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_user)
    db.session.commit()