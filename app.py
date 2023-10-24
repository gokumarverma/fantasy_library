
from fantasy_lab import app
from flask import render_template, url_for
from fantasy_lab.models import Authors,Books


@app.route("/")
def home():
    return render_template("home.html")
    

@app.route("/list_all")
def list_all():
    authors = Authors.query.all()
    books = Books.query.all()
    return render_template("list_all.html", authors=authors, books=books)
    


if __name__ == "__main__":
    app.run(debug=True)


