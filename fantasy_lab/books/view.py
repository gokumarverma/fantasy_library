from flask import Blueprint, redirect, render_template, url_for
from fantasy_lab.models import db, Books
from fantasy_lab.books.forms import AddFrom,RemoveForm

books_blp=Blueprint("books",__name__, template_folder='templates/books')

@books_blp.route("/add_book", methods=["GET", "POST"])
def add():
    form = AddFrom()
    if form.validate_on_submit():
        name = form.name.data
        author_id = form.author_id.data
        new_book = Books(name, author_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books.all'))
    return render_template("add_book.html", form=form)


@books_blp.route("/remove_book", methods=["GET", "POST"])
def remove():
    form = RemoveForm()
    if form.validate_on_submit():
        id = form.id.data
        book = Books.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('books.all'))
    return render_template("remove_book.html", form=form)


@books_blp.route("/all")
def all():
    books = Books.query.all()
    return render_template("all_books.html", books=books)