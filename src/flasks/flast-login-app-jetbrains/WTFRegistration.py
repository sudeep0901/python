from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators
from wtforms_components import ColorField

from wtforms.fields.html5 import EmailField


class RegistrationForm(FlaskForm):
    email = EmailField('email',
                       validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(),
                                                     validators.Length(min=8,
                                                                       message="Please choose a password of at least "
                                                                               "8 characters")])

    password2 = PasswordField('password2',
                              validators=[validators.DataRequired(),
                                          validators.EqualTo('password', message='Passwords must match')])
    background_color = ColorField()

    submit = SubmitField('submit', [validators.DataRequired()])
