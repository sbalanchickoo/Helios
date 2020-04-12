from foodjournal import create_app, db
from flask_script import Manager, prompt_bool
from flask import Blueprint

app = create_app()

with app.app_context():
    from foodjournal.models import *
    from foodjournal.views.core import core
    app.register_blueprint(core, url_prefix='/')


manager = Manager(app)

if __name__ == '__main__':
    app.run()
