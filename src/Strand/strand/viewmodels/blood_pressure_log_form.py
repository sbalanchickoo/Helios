from flask_wtf import Form
from wtforms.fields import StringField, DecimalField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from datetime import datetime


class BloodPressureForm(Form):
    systolic = IntegerField(label='Systolic '
                               , validators=[DataRequired(), NumberRange(min=0, max=200)])
    diastolic = IntegerField(label='Diastolic '
                                    , validators=[DataRequired(), NumberRange(min=0, max=200)])
    heart_rate = IntegerField(label='Heart rate '
                             , validators=[DataRequired(), NumberRange(min=0, max=100)])
    date = DateField(label='Date ', default=datetime.utcnow()
                     , validators=[DataRequired(message='Enter a valid date'), ])
    notes = StringField(label='Additional notes')
