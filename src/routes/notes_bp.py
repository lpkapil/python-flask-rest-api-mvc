from flask import Blueprint
from controllers.NotesController import create, read_one, update, delete

notes_bp = Blueprint('notes_bp', __name__)
notes_bp.route('/', methods=['POST'])(create)
notes_bp.route('/<int:note_id>', methods=['GET'])(read_one)
notes_bp.route('/<int:note_id>/edit', methods=['POST'])(update)
notes_bp.route('/<int:note_id>', methods=['DELETE'])(delete)