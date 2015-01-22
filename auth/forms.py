from flask.ext.mongoengine.wtf import model_form
from wtforms.fields import StringField, PasswordField, SubmitField
from flask.ext.mongoengine.wtf.orm import validators
from flask_wtf import Form
from wtforms.validators import DataRequired, Regexp, Email

from . import models


# Signup Form created from user_form
class SignupForm(Form):
	username = StringField('username', validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ''numbers, dots or underscores')])
	password = PasswordField('Password:', validators=[validators.Required(), validators.EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Repeat Password')
	email = StringField('Email', validators = [validators.Required(), Email()])
	submit = SubmitField('Submit')

# Login form will provide a Password field (WTForm form field)
class LoginForm(Form):
	username = StringField('username', validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ''numbers, dots or underscores')])
	password = PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Submit')
