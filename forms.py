from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, IntegerField, SubmitField, FileField, \
    BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo


class UserForm(FlaskForm):
    name = StringField('* Name', validators=[DataRequired()])
    surname = StringField('* Surname', validators=[DataRequired()])
    email = StringField('* Email', validators=[DataRequired(), Email(message='Bad email')])
    username = StringField('* Username', validators=[DataRequired()])
    description = TextAreaField('Tell us about yourself',
                                render_kw={'class': 'form-control', 'rows': 10})
    age = IntegerField('* Age', validators=[DataRequired()])


class RegisterUserForm(UserForm):
    password = PasswordField('* Password', validators=[DataRequired()])
    password_again = PasswordField('* Password again',
                                   validators=[DataRequired(), EqualTo('password',
                                                                       message='Passwords do not match')])
    country = SelectField('* Country', coerce=str, validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField('Register')


class EditUserForm(UserForm):
    submit = SubmitField('Save')


class LoginForm(FlaskForm):
    username_email = StringField('Username or email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')


class ProjectForm(FlaskForm):
    name = StringField('* Project name', validators=[DataRequired()])
    image_field = FileField('Project image')
    short_description = TextAreaField('* Short description', validators=[DataRequired()])
    full_description = TextAreaField('Full description',
                                     render_kw={'class': 'form-control', 'rows': 20})
    collaborators = StringField(
        'Collaborators')


class RegisterProjectForm(ProjectForm):
    submit = SubmitField('Create project')


class EditProjectForm(ProjectForm):
    submit = SubmitField('Save')


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Leave a comment')
