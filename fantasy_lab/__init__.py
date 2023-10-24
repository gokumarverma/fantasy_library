### this is the __init__.py file under fantasy_library folder ###
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Integer,String
from flask_migrate import Migrate

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"]="billpagers"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,"db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

Migrate(app,db)

from fantasy_lab.authors.view import authors_blp
from fantasy_lab.books.view import books_blp
app.register_blueprint(authors_blp,url_prefix="/authors")
app.register_blueprint(books_blp,url_prefix="/books")

