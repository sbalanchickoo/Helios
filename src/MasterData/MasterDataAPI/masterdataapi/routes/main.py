from time import gmtime, strftime
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return "Hello world, it is " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
