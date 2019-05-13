from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField, SelectField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from app.models import User
# from flask_babel import lazy_gettext as _l


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName= StringField('Last Name')

    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    # password2 =PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(),  EqualTo('password')])
    
    ad_street=StringField('Street Address')
    ad_suburb=StringField('City/Suburb')
    ad_state=SelectField('State', choices=[('WA','Western Australia'), ('QLD','Queensland'), ('SA','South Australia'),('ACT','Australian Capital Territory'),('NT','Northern Territory'), ('TAS','Tasmania')], default='WA')
    ad_country=SelectField('Country', choices=[('Aus','Australia')])

    
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username= username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins