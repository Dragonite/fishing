from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField
from app.models import User


class LoginForm(FlaskForm):
    logInId = StringField('Username', validators=[DataRequired()])
    pwd = PasswordField('Password', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    pwd_repeat=PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_username(self,logInId):
        user = User.query.filter_by(logInId=logInId.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins