from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from app.models import User
from flask_babel import _, lazy_gettext as _l



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    # password2 =PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    password2 = PasswordField(_l('Repeat Password'), validators=[DataRequired(),  EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by( username= username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins

# class CreatePollForm(FlaskForm):
#     title = TextAreaField('Title', validators=[DataRequired()])
#     description = TextAreaField('Description', validators=[DataRequired()])
#     choice = StringField('Create Choices', validators=[DataRequired()])
#     options = FieldList(StringField('Choice'), min_entries=10,max_entries=10)
#     isOpen = BooleanField('Open Poll', validators=[DataRequired()])
#     submit = SubmitField('Create Poll')
