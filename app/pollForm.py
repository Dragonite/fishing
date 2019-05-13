from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField
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



class CreateResponseForm(FlaskForm):
    parameter=[]
    def __init__(self, candidateParameter):
        self.parameter=candidateParameter


    pollId=IntegerField()
    userId=IntegerField()
    candidateId= FieldList(IntegerField())
    response= FieldList(IntegerField())
    submit = SubmitField('Submit my response')
    responses = FieldList('Responses', choices=[(c[0], c[1]) for c in parameter], coerce=int)
