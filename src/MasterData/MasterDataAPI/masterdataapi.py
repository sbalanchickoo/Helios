from flask import Flask, jsonify
from config import Config, db
from views.dataretrieve import get_country, get_state

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/state")
def us_state():
    return get_state()


@app.route("/country")
def country():
    return get_country()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
