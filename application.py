import os, requests, json

from flask import Flask, session, render_template, jsonify, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/home")
def home():
    books = db.execute("SELECT * FROM books")
    return jsonify(books)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration")
def registration():
    return "registration"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<int:userid>")
def userHome(userid):
    user = db.execute("SELECT * FROM USERS where id = :id", {"id": userid}).fetchone();
    return jsonify(username = user.username, password = user.password, id = user.id) 

@app.route("/api/<string:isbn>")
def apiResponse(isbn):
    book = db.execute("SELECT * FROM BOOKS where isbn = :isbn",{"isbn": isbn}).fetchone()
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "GOFxeuRmezPXoTFLVIAs4A", "isbns": isbn})
    response = res.json()
    res_dict = json.loads(response)

    return jsonify(title= book.title, author = book.author, year = book.year, isbn = book.isbn, review_count = res_dict['ratings_count'], average_score = res_dict['average_rating'])