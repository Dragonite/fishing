from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField
from wtforms.validators import DataRequired, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CreatePollForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    choice = StringField('Create Choices', validators=[DataRequired()])
    options = FieldList(StringField('Choice'), min_entries=10,max_entries=10)
    isOpen = BooleanField('Open Poll', validators=[DataRequired()])
    submit = SubmitField('Create Poll')
