from flask import Blueprint

PostsAPI = Blueprint('PostsAPI', __name__, url_prefix="/posts")

@PostsAPI.route("/", methods=["GET"])
def get_posts():
    return "Hello Posts"
