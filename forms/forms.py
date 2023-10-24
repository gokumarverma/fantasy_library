from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddBook(FlaskForm):
    name=StringField("Enter book name to add: ")
    author_id=IntegerField("Enter Author Id: ")
    submit=SubmitField("Add Book")

class AddAuthor(FlaskForm):
    name=StringField("Enter name of Author to add: ")
    submit=SubmitField("Add Author")

class RemoveBook(FlaskForm):
    id=IntegerField("Enter the book id to remove: ")
    submit=SubmitField("Remove Book")

class RemoveAuthor(FlaskForm):
    id=IntegerField("Enter the author id to remove: ")
    submit=SubmitField("Remove Author")
