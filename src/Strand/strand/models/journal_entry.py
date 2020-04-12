# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc

# Local application imports
from strand import db


class JournalEntry(db.Model):
    __tablename__ = 'JournalEntry'
    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    thankful = db.Column('ThankfulFor', db.String, nullable=False)
    location = db.Column('Location', db.String(300), nullable=False)
    highlights = db.Column('Highlights', db.String(300), nullable=False)
    notes = db.Column('Notes', db.String(), nullable=True)

    # foreign key name is table name.id
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    @staticmethod
    def newest(num):
        return JournalEntry.query.order_by(desc(JournalEntry.date)).limit(num)

    @staticmethod
    def all():
        return JournalEntry.query.order_by(desc(JournalEntry.date))


# def __repr__(self):
#    return "<Bookmark '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'thankful': self.thankful,
            'location': self.location,
            'highlights': self.highlights,
            'notes': self.notes
         }
