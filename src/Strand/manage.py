import os
from flask_script import Manager, prompt_bool
from strand import create_app, db
from strand.models.user import User
from flask_migrate import Migrate, MigrateCommand, init
from strand.config import Config
from pathlib import Path

app = create_app()
with app.app_context():
    # Import models and views so that the create all statement will include them
    from strand.models import \
        blood_pressure_log \
        , body_part_metadata \
        , exercise_log \
        , exercise_metadata \
        , metrics_log \
        , user
    from strand.views.core import core_blueprint
    app.register_blueprint(core_blueprint, url_prefix='/')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init_db():
    db.create_all()
    initial_users = ['shri']
    for initial_user in initial_users:
        user_entry = User.get_by_username('shri')
        if not user_entry:
            db.session.add(User(username='shri', password='shri', email='shri@gmail.com'))
            db.session.commit()
    print('Initialized the database')


@manager.command
def drop_db():
    if prompt_bool("Are you sure you want to drop the DB"):
        db.drop_all()
        print('Dropped the database')


if __name__ == '__main__':
    manager.run()
