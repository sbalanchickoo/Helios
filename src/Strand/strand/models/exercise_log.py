# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc

# Local application imports
from strand import db


class ExerciseLog(db.Model):
    __tablename__ = 'ExerciseLog'
    id = db.Column('id', db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    completed_flag = db.Column('CompletedFlag', db.Boolean, nullable=False)
    time_seconds = db.Column('TimeSeconds', db.Integer, nullable=True)
    weight_kg = db.Column('WeightKG', db.Float, nullable=True)
    reps = db.Column('Reps', db.Integer, nullable=True)
    notes = db.Column('Notes', db.String(300))
    # foreign key name is table name.id
    exercise_id = db.Column(db.Integer, db.ForeignKey('ExerciseMetadata.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    @staticmethod
    def newest(num):
        return ExerciseLog.query.order_by(desc(ExerciseLog.date)).limit(num)

    @staticmethod
    def all():
        return ExerciseLog.query.order_by(desc(ExerciseLog.date))

    # @staticmethod
    # def __repr__(self):
    #    return "<Weight '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'completed_flag': self.completed_flag,
            'time_seconds': self.time_seconds,
            'weight_kg': self.weight_kg,
            'reps': self.reps,
            'notes': self.notes
         }
