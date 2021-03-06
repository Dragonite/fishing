from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField, SelectField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from app.models import User
# from flask_babel import _, lazy_gettext as _l



class LoginForm(FlaskForm):
    username = StringField('Username',  validators=[DataRequired(), validators.Length(min=3, max=64)])
    password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=3, max=64)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


