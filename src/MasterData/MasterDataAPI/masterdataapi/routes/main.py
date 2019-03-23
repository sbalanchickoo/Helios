from masterdataapi import app
from time import gmtime, strftime


@app.route("/")
def index():
    return "Hello world, it is " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
