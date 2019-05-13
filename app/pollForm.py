from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, IntegerField
from wtforms.validators import  ValidationError, DataRequired, Email, EqualTo, NumberRange
from wtforms.fields.html5 import EmailField
from app.models import User
# from flask_babel import _, lazy_gettext as _l



class CreatePollForm(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    choice = StringField('Create Choices')
    options = FieldList(StringField('Choice'), min_entries=10, max_entries=10)
    isOpen = BooleanField('Open Poll')

    minResponses=IntegerField('Minimum responses to collect')

    submit = SubmitField('Create Poll')



class CreateResponseForm(FlaskForm):
    poll=Poll.query.
    def __init__(self, poll):
        self.poll=poll


    pollId=IntegerField()
    userId=IntegerField()
    candidateId= FieldList(IntegerField())
    response= FieldList(IntegerField())
    submit = SubmitField('Submit my response')
    responses = FieldList('Responses', choices=[(c.candidateId, c.candidateDescription) for c in poll.Candidate])
