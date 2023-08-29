# NoteSchema.py

from config import db, ma
from models.UserModel import Note

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True

note_schema = NoteSchema()



