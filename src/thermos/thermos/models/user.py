from run import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return "<User %r>" % self.username

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
