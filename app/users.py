from flask import Blueprint

UsersAPI = Blueprint('UsersAPI', __name__, url_prefix="/users")

@UsersAPI.route("/", methods=["GET"])
def get_users():
    return "Hello Users"
