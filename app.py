from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient


# ...

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

client = pymongo.MongoClient(mongodb+srv://beneres:<password>@cluster0.07a8zoq.mongodb.net/test)

db = client.flask_db
todos = db.todos

# collections
todos = db.todos

records = db.register

# ...



@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')