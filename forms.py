from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User,Contact2,Contact
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    message= StringField(label='Message')
    submit = SubmitField(label="Send")


    def validate_email(self, email):
        user = Contact.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('You have already sent one. I will contact you very shortly')
    def validate_name(self, name):
        user = Contact.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('You have already sent one. I will contact you very shortly')

class Contact2Form(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    project_choice = SelectField('project', choices =[(1,'project1(EECS281)'),(2,'project2(EECS281)'),
                                                      (3,'project3(EECS281)'),(4,'project4(EECS281)'),
                                                      (5,'project1(EECS370)'),(6,'project2(EECS370)'),
                                                      (7,'project3(EECS370)'),(8,'project4(EECS370)')])
    Agree = StringField(label='Agree', validators=[DataRequired()])
    submit = SubmitField(label="Send")

    def validate_email(self, email):
        user = Contact2.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('You have already sent one. I will contact you very shortly')
    def validate_name(self, name):
        user = Contact2.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('You have already sent one. I will contact you very shortly')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
