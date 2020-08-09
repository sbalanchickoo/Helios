from flask_wtf import Form
from wtforms.fields import StringField, DecimalField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from datetime import datetime
from ..models.blood_pressure_log import BloodPressureLog


class BloodPressureLogForm(Form):
    systolic = IntegerField(label='Systolic ', validators=[DataRequired(), NumberRange(min=0, max=200)])
    diastolic = IntegerField(label='Diastolic ', validators=[DataRequired(), NumberRange(min=0, max=200)])
    heart_rate = IntegerField(label='Heart rate ', validators=[DataRequired(), NumberRange(min=0, max=100)])
    date = DateField(label='Date ', default=datetime.utcnow(), validators=[DataRequired(message='Enter a valid date')])
    notes = StringField(label='Additional notes')

    @staticmethod
    def validate_date(form, field):
        min_time = datetime.min.time()
        field_data_datetime = datetime.combine(field.data, min_time)
        entry = BloodPressureLog.get_by_date(date_string=field_data_datetime)
        if len(entry.all()) > 0:
            raise ValidationError('Entry for this date already exists!')
