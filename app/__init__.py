from flask import Flask

from .users import UsersAPI
from .posts import PostsAPI
from .tokens import TokensAPI

app = Flask(__name__)

app.register_blueprint(UsersAPI)
app.register_blueprint(PostsAPI)
app.register_blueprint(TokensAPI)

@app.route("/")
def hello():
    return "Hello World !"
