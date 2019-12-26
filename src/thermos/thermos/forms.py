from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, url
from wtforms.fields.html5 import URLField


class BookMarkForm(Form):
    url = URLField('url', validators=[DataRequired(), url()])
    description = StringField('description')

# Customize data validation
    def validate(self):
        if not self.url.data.startswith("http://") or \
                self.url.data.startswith("https://"):
            self.url.data = "http://" + self.url.data
        if not self.description.data:
            self.description.data = self.url.data
        return True


class LoginForm(Form):
    username = StringField('Your User Name:', validators=[
                           DataRequired("Please Enter user name to register or login")])
    password = PasswordField('Please Enter Password:',
                             validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')
