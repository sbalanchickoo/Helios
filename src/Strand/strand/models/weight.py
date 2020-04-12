# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc

# Local application imports
from strand import db


class Weight(db.Model):
    __tablename__ = 'Weight'
    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    body_weight = db.Column('Weight', db.Float, nullable=True)
    bmi = db.Column('BMI', db.Float, nullable=True)
    body_fat_percent = db.Column('BodyFatPercent', db.Float, nullable=True)
    notes = db.Column('Notes', db.String(300))
    # foreign key name is table name.id
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    @staticmethod
    def newest(num):
        return Weight.query.order_by(desc(Weight.date)).limit(num)

    @staticmethod
    def all():
        return Weight.query.order_by(desc(Weight.date))

    # @staticmethod
    # def __repr__(self):
    #    return "<Weight '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'body_weight': self.body_weight,
            'bmi': self.bmi,
            'body_fat_percent': self.body_fat_percent,
            'notes': self.notes
         }
