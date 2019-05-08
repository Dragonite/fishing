from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from app.models import User
from flask_babel import _, lazy_gettext as _l



class CreatePollForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    choice = StringField('Create Choices')
    options = FieldList(StringField('Choice'), min_entries=10, max_entries=10)
    isOpen = BooleanField('Open Poll')
    submit = SubmitField('Create Poll')
