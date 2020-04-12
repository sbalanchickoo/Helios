from flask_wtf import Form
from wtforms.fields import StringField, DecimalField, SubmitField, DateField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from datetime import datetime


class WeightForm(Form):
    body_weight = DecimalField(label='Weight (KG) '
                               , validators=[DataRequired(), NumberRange(min=0, max=300)])
    body_fat_percent = DecimalField(label='Body fat percent '
                                    , validators=[DataRequired(), NumberRange(min=0, max=100)])
    date = DateField(label='Date ', default=datetime.utcnow()
                     , validators=[DataRequired(message='Enter a valid date'), ])
    notes = StringField(label='Additional notes')

    @staticmethod
    def validate_body_weight(form, field):
        if not field.data > 0 and field.data < 120.0:
            raise ValidationError('Body weight must be positive number')
        return True

    @staticmethod
    def validate_body_fat_percent(form, field):
        if not field.data > 0 and field.data < 100.0:
            raise ValidationError('Body fat percent must be 0-100')
        return True
