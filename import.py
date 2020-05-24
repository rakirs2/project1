import csv
import os, csv
from models import *
#just reimporting to avoid cautions
from models import Book, User, Review, db

import requests

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request



#create db table
#readbooks
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    db.create_all()

    f= open("books.csv")
    reader = csv.reader(f)
    count = 0
    for isbn, title, author, year in reader:
        book = Book(isbn=isbn, title= title, author= author, year= year)
        db.session.add(book);
        print(f"{count} Read {isbn} {title}, {author}, {year}")
        count+=1
        db.session.commit();
    f.close();

    f = open("users.csv")
    reader = csv.reader(f)
    for username, password in reader:
        user = User(username=username, password=password)
        db.session.add(user)
        print(f"{user.username}, {user.password}")
        db.session.commit();
        

if __name__ == "__main__":
    with app.app_context():
        main()
