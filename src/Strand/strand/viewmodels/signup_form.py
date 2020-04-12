from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp, ValidationError
from ..models.user import User


class SignupForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(3, 80),
            Regexp('^[A-Za-z0-9_]{3,}$', message = 'Username must contain letters, numbers, underscore')])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(8, 80),
            EqualTo('password2', 'passwords must match')])
    password2 = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired()])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Length(1, 120),
            Email(message='Must be a valid email')])
    submit = SubmitField(label='Add User')

    @staticmethod
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('This email already exists')

    @staticmethod
    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username already exists')