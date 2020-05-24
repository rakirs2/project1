from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__= "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable = False)
    title = db.Column(db.String,  nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.Integer, nullable = False)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

class Review(db.Model):
    __tablename__="reviews"
    id = db.Column(db.Integer, primary_key = True)
    User_id= db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable =False)
    rating = db.Column(db.Integer, db.CheckConstraint('rating<5 AND rating>1'))
    text = db.Column(db.String, nullable = False)