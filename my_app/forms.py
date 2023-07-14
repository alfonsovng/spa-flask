from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

def trim(s):
    if s is None:
        return None
    return s.strip()

class LoginForm(FlaskForm):
    email = StringField(
        validators=[DataRequired()],
        filters = [trim]
    )
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()
