from datetime import datetime


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


@app.route('/<name>/<location>')
def index(name, location):
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()

    return '<h1>Added New User!</h1>'

@app.route('/<name>')
def get_user(name):
    user = User.query.filter_by(name=name).first()
    
    return '<h1>The User is Located in: {user=location}</h1>'