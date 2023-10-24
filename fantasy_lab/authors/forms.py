from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    name = StringField("Enter name of Author to add: ")
    submit = SubmitField("Add Author")

class RemoveForm(FlaskForm):
    id = IntegerField("Enter the author id to remove: ")
    submit = SubmitField("Remove Author")