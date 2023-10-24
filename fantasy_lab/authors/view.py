from flask import Blueprint, url_for, redirect, render_template
from fantasy_lab import db
from fantasy_lab import models
from fantasy_lab.models import Authors
from fantasy_lab.authors.forms import AddForm, RemoveForm

authors_blp = Blueprint('authors', __name__,
                        template_folder="templates/authors")

@authors_blp.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_author = Authors(name)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('authors.all'))
    return render_template("add_author.html", form=form)


@authors_blp.route("/remove", methods=["GET", "POST"])
def remove():
    form = RemoveForm()
    if form.validate_on_submit():
        id = form.id.data
        author = Authors.query.get(id)
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('authors.all'))
    return render_template("remove_author.html", form=form)

@authors_blp.route("/all", methods=["GET","POST"])
def all():
    authors = Authors.query.all()
    return render_template("all_authors.html", authors=authors)
