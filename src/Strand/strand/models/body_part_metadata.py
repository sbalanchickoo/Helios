# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc
from sqlalchemy.orm import relationship

# Local application imports
from strand import db


class BodyPartMetadata(db.Model):
    __tablename__ = 'BodyPartMetadata'
    id = db.Column('id', db.Integer, primary_key=True)
    body_part_name = db.Column('BodyPartName', db.String(255), nullable=False)
    notes = db.Column('Notes', db.String(300))

    @staticmethod
    def newest(num):
        return BodyPartMetadata.query.order_by(desc(BodyPartMetadata.date)).limit(num)

    @staticmethod
    def all():
        return BodyPartMetadata.query.order_by(desc(BodyPartMetadata.date))

    # def __repr__(self):
    #    return "<Bookmark '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'body_part_name': self.body_part_name,
            'notes': self.notes
        }
