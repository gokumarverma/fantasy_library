# --- MODELS --- #
### set up db in the  __init__.py file under fantasy_library folder ###
from fantasy_lab import db, ForeignKey, relationship, Integer, String
from fantasy_lab import app

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    author_id = db.Column(db.Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Authors", back_populates="books", uselist=False)

    def __init__(self, name, author_id):
        self.name = name
        self.author_id = author_id

    def __repr__(self):
        return self.name


class Authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    books = relationship("Books", back_populates="author",
                         cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

with app.app_context():
    db.create_all()