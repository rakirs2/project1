import csv
import os, csv
from models import *
from models import Book

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

db = SQLAlchemy()


#create db table
#readbooks
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    f= open("books.csv")
    reader = csv.reader(f)
    count = 0
    for isbn, title, author, year in reader:
        book = Book(isbn=isbn, title= title, author= author, year= year)
        db.session.add(book);
        print(f"Read {isbn} {title}, {author}, {year}")
        count+=1
        db.session.commit();

if __name__ == "__main__":
    with app.app_context():
        main()
