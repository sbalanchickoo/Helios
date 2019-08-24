from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField(label='Please enter Username', validators=[DataRequired()])
    password = PasswordField(label='Please enter Password', validators=[DataRequired()])
    remember_me = BooleanField(label='Remember me')
    submit = SubmitField(label='Submit')
