from config import db


class USState(db.Model):
    __tablename__ = 'State'
    id = db.Column(db.Integer, primary_key = True)
    abbrev = db.Column(db.String(2))
    state = db.Column(db.String(128))

    def __repr__(self):
        return 'Abbreviation: {}; Name: {}'.format(self.abbrev, self.state)

    @property
    def serialize(self):
        return {
            'abbrev': self.abbrev,
            'fullname': self.state
        }
