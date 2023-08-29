# NotesController.py

from flask import abort, make_response
from config import db
from models.UserModel import User, Note
from models.schema.NoteSchema import note_schema

# Create Note
def create(note):
    user_id = note.get("user_id")
    user = User.query.get(user_id)

    if user:
        new_note = note_schema.load(note, session=db.session)
        user.notes.append(new_note)
        db.session.commit()
        return note_schema.dump(new_note), 201
    else:
        abort(
            404,
            f"User not found for user ID: {user_id}"
        )

# Read Note       
def read_one(note_id):
    note = Note.query.get(note_id)
    if note is not None:
        return note_schema.dump(note)
    else:
        abort(
            404, f"Note with ID {note_id} not found"
        )

# Update Note
def update(note_id, note):
    existing_note = Note.query.get(note_id)
    if existing_note:
        existing_note.content = note["content"]
        db.session.merge(existing_note)
        db.session.commit()
        return note_schema.dump(existing_note), 201
    else:
        abort(404, f"Note with ID {note_id} not found")

# Delete Note
def delete(note_id):
    existing_note = Note.query.get(note_id)
    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"{note_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {note_id} not found")