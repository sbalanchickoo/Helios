from flask import Flask
from config import Config, db
from views.dataretrieve import get_state, get_country

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/")
def index():
    return "Hello world 13!"


@app.route("/state")
def us_state():
    return get_state()


@app.route("/country")
def country():
    return get_country()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
