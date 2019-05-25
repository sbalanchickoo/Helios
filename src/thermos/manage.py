# Third party imports
from flask_script import Manager, prompt_bool

# Local application imports
from thermos import db
from thermos.models.user import User
from thermos.run import app

manager = Manager(app)


@manager.command
def init_db():
    db.create_all()
    db.session.add(User(username='Shri', email='shri@gmail.com'))
    db.session.add(User(username='Sam', email='sam@gmail.com'))
    db.session.commit()
    print('Initialized the database')


@manager.command
def drop_db():
    if prompt_bool("Are you sure you want to drop the DB"):
        db.drop_all()
        print('Dropped the database')


if __name__ == '__main__':
    manager.run()

