# Standard library imports
from datetime import datetime

# Third party imports
from sqlalchemy import desc
from sqlalchemy.orm import relationship

# Local application imports
from strand import db


class ExerciseMetadata(db.Model):
    __tablename__ = 'ExerciseMetadata'
    id = db.Column('id', db.Integer, primary_key=True)
    exercise_name = db.Column('ExerciseName', db.String(255), nullable=False)
    notes = db.Column('Notes', db.String(300))
    # foreign key name is table name.id
    body_part_worked_1 = db.Column(db.Integer, db.ForeignKey('BodyPartMetadata.id'), nullable=False)
    body_part_worked_2 = db.Column(db.Integer, db.ForeignKey('BodyPartMetadata.id'), nullable=True)
    body_part_worked_3 = db.Column(db.Integer, db.ForeignKey('BodyPartMetadata.id'), nullable=True)

    body_part_worked_1_rel = db.relationship('BodyPartMetadata'
                                             , backref='part1'
                                             , foreign_keys=[body_part_worked_1])
    body_part_worked_2_rel = db.relationship('BodyPartMetadata'
                                             , backref='part2'
                                             , foreign_keys=[body_part_worked_2])
    body_part_worked_3_rel = db.relationship('BodyPartMetadata'
                                             , backref='part3'
                                             , foreign_keys=[body_part_worked_3])

    # backref can be anything, either the class name or table name
    exercise_log_rel = db.relationship('ExerciseLog', backref='ExerciseMetadata', lazy='dynamic')

    @staticmethod
    def newest(num):
        return ExerciseMetadata.query.order_by(desc(ExerciseMetadata.date)).limit(num)

    @staticmethod
    def all():
        return ExerciseMetadata.query.order_by(desc(ExerciseMetadata.date))

    # @staticmethod
    # def __repr__(self):
    #    return "<Weight '{}: '{}'>".format(self.description, self.url)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.exercise_name,
            'body_part_worked_1': self.body_part_worked_1,
            'body_part_worked_2': self.body_part_worked_2,
            'body_part_worked_3': self.body_part_worked_3,
            'notes': self.notes
        }