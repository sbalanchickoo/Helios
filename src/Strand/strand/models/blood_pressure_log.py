# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc

# Local application imports
from strand import db


class BloodPressureLog(db.Model):
    __tablename__ = 'BloodPressureLog'
    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    systolic = db.Column('Systolic', db.Integer, nullable=False)
    diastolic = db.Column('Diastolic', db.Integer, nullable=False)
    heart_rate = db.Column('HeartRate', db.Integer, nullable=False)
    notes = db.Column('Notes', db.String(300))
    # foreign key name is table name.id
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    @staticmethod
    def newest(num):
        return BloodPressureLog.query.order_by(desc(BloodPressureLog.date)).limit(num)

    @staticmethod
    def all():
        return BloodPressureLog.query.order_by(desc(BloodPressureLog.date))

    @staticmethod
    def get_by_date(date_string):
        return BloodPressureLog.query.filter(BloodPressureLog.date == date_string)


# def __repr__(self):
#    return "<Bookmark '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'systolic': self.systolic,
            'diastolic': self.diastolic,
            'heart_rate': self.heart_rate,
            'notes': self.notes
         }
