from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from app.models import User, Poll
# from flask_babel import _, lazy_gettext as _l
from app import db
from app.main import bp
from flask import current_app

class CreatePollForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    choice = StringField('Create Choices')
    options = FieldList(StringField('Choice'), min_entries=10, max_entries=10)
    isOpen = BooleanField('Open Poll')

    minResponses=IntegerField('Minimum responses to collect')

    submit = SubmitField('Create Poll')


def makeResponseForm(responseParameter):
    class ResponseForm(FlaskForm):
        # responses=SelectField('choices', choices=responseParameter)
        # # pref = FieldList(StringField('Preference'), min_entries=len(responseParameter), max_entries=len(responseParameter))
        preferences = FieldList(SelectField('Preference', choices=responseParameter), min_entries=len(responseParameter),
                         max_entries=len(responseParameter))
        submit = SubmitField('Submit Vote')
    return ResponseForm()