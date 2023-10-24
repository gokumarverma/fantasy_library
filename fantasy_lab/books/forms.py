from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class AddFrom(FlaskForm):
    name = StringField("Enter book name to add: ")
    author_id = IntegerField("Enter Author Id: ")
    submit = SubmitField("Add Book")


class RemoveForm(FlaskForm):
    id = IntegerField("Enter the book id to remove: ")
    submit = SubmitField("Remove Book")
