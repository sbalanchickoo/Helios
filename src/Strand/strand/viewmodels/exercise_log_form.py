from flask_wtf import Form
from wtforms.fields import \
    StringField\
    , DecimalField\
    , SubmitField\
    , DateField\
    , IntegerField\
    , BooleanField\
    , SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from datetime import datetime


class ExerciseLogForm(Form):
    exercise_id = SelectField('Exercise ', coerce=int)
    completed_flag = BooleanField(label='Completed ')
    time_seconds = IntegerField(label='Time (seconds) '
                                , validators=[NumberRange(min=0, max=3600)]
                                , default=0)
    time_minutes = DecimalField(label='Time (minutes) '
                                , validators=[NumberRange(min=0, max=1440)]
                                , default=0)
    weight_kg = DecimalField(label='Weight (kg) '
                             , default=0
                             , validators=[NumberRange(min=0, max=100)])
    weight_lb = DecimalField(label='Weight (lb) '
                             , default=0
                             , validators=[NumberRange(min=0, max=100)])
    reps = IntegerField(label='Reps '
                                , validators=[NumberRange(min=0, max=100)]
                                , default=0)
    date = DateField(label='Date ', default=datetime.utcnow()
                     , validators=[DataRequired(message='Enter a valid date'), ])
    notes = StringField(label='Notes ')
