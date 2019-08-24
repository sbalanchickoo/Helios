# Third party imports
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

# Local application imports
from thermos import db, create_app
app = create_app()
# from thermos.run import app
# from thermos.models.user import User
# from thermos.models.bookmark import Bookmark
# from thermos.models.tags import Tag

# with app.app_context():
    # Import models and views so that the create all statement will include them
    # from thermos.models.user import User
    # from thermos.models.bookmark import Bookmark
    # from thermos.models.tags import Tag

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def init_db():
    db.create_all()
    # db.session.add(User(username='shri', password='sb', email='shri@gmail.com'))
    # db.session.add(User(username='john', password='sb', email='john@gmail.com'))
    db.session.commit()
    print('Initialized the database')


@manager.command
def drop_db():
    if prompt_bool("Are you sure you want to drop the DB"):
        db.drop_all()
        print('Dropped the database')


if __name__ == '__main__':
    manager.run()

