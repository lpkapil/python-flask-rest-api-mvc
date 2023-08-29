# UserSchema.py

from config import db, ma
from models.UserModel import User
from models.schema.NoteSchema import NoteSchema
from marshmallow_sqlalchemy import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    notes = fields.Nested(NoteSchema, many=True)
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)


