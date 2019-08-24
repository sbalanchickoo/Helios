# Standard library imports

# Third party imports

# Local application imports
from thermos import db


class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column('id', db.Integer, primary_key=True)
    label = db.Column('label', db.Text, nullable=False)
