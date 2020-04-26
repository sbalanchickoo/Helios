# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc

# Local application imports
from strand import db


class MetricsLog(db.Model):
    __tablename__ = 'MetricsLog'
    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    weight_kg = db.Column('WeightKG', db.Float, nullable=True)
    bmi = db.Column('BMI', db.Float, nullable=True)
    body_fat_percent = db.Column('BodyFatPercent', db.Float, nullable=True)
    notes = db.Column('Notes', db.String(300))
    # foreign key name is table name.id
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    @staticmethod
    def newest(num):
        return MetricsLog.query.order_by(desc(MetricsLog.date)).limit(num)

    @staticmethod
    def all():
        return MetricsLog.query.order_by(desc(MetricsLog.date))

    # @staticmethod
    # def __repr__(self):
    #    return "<Weight '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'weight_kg': self.weight_kg,
            'bmi': self.bmi,
            'body_fat_percent': self.body_fat_percent,
            'notes': self.notes
         }
