from flask import Blueprint
from controllers.UsersController import read_all, create, update, delete, read_one

users_bp = Blueprint('users_bp', __name__)
users_bp.route('/', methods=['GET'])(read_all)
users_bp.route('/', methods=['POST'])(create)
users_bp.route('/<string:email>', methods=['GET'])(read_one)
users_bp.route('/<string:email>/edit', methods=['PUT'])(update)
users_bp.route('/<int:user_id>', methods=['DELETE'])(delete)