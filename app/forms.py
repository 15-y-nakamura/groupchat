from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField, BooleanField,
    SubmitField, StringField, TextAreaField)
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):

    username = StringField('Username')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class MessageForm(FlaskForm):

    message = TextAreaField('Message:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ChatroomForm(FlaskForm):

    room_name = StringField('Chatroom name:', validators=[DataRequired()])
    submit = SubmitField('Create chatroom')

class FriendRequestForm(FlaskForm):

    code = StringField('Code')
    submit = SubmitField('Reuqest')
    
class UserForm(FlaskForm):

    username = StringField('Username')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password')
    code = StringField('Code')
    submit = SubmitField('Update')

class GroupMessageForm(FlaskForm):

    message = TextAreaField('Message:', validators=[DataRequired()])
    submit = SubmitField('Submit')
