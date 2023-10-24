import os
from forms.forms import AddAuthor, AddBook, RemoveBook, RemoveAuthor
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy, session
#from models.models import Books, Author
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer


basedir=os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"]="billpagers"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+ os.path.join(basedir,"database.sqlite")

db=SQLAlchemy(app)
class Books(db.Model):
    __tablename__="books"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False, unique=True)
    author_id=db.Column(db.Integer, ForeignKey("authors.id"), nullable=False)
    author=relationship("Authors", back_populates="books", uselist=False)

    def __init__(self,name,author_id):
        self.name=name
        self.author_id=author_id
    
    def __repr__(self):
        return self.name
    
class Authors(db.Model):
    __tablename__="authors"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False,unique=True)
    books=relationship("Books",back_populates="author", cascade="all, delete-orphan" )


    def __init__(self,name):
        self.name=name
    
    def __repr__(self):
        return self.name
    
with app.app_context():
    db.create_all()
    

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_book", methods=["GET","POST"])
def add_book():
    form=AddBook()
    if form.validate_on_submit():
        name=form.name.data
        author_id=form.author_id.data
        new_book=Books(name,author_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect (url_for('all_books'))
    return render_template("add_book.html", form=form)

@app.route("/add_author", methods=["GET","POST"])
def add_author():
    form=AddAuthor()
    if form.validate_on_submit():
        name=form.name.data
        new_author=Authors(name)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('all_authors'))
    return render_template("add_author.html", form=form)


@app.route("/remove_book",methods=["GET","POST"])
def remove_book():
    form=RemoveBook()
    if form.validate_on_submit():
        id=form.id.data
        book =Books.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('all_books'))
    return render_template("remove_book.html",form=form)

@app.route("/remove_author",methods=["GET","POST"])
def remove_author():
    form=RemoveAuthor()
    if form.validate_on_submit():
        id=form.id.data
        author=Authors.query.get(id)
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('all_authors'))
    return render_template("remove_author.html",form=form)

@app.route("/list_all")
def list_all():
    authors=Authors.query.all()
    books=Books.query.all()

    return render_template("list_all.html", authors=authors,books=books)

@app.route("/all_books")
def all_books():
    books=Books.query.all()
    return render_template("all_books.html", books=books)

@app.route("/all_authors")
def all_authors():
    authors=Authors.query.all()
    return render_template("all_authors.html", authors=authors)


if __name__ == "__main__":
    app.run(debug=True)
