from flask_login import UserMixin
from datetime import datetime
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    workouts = db.relationship('Workout', backref='author', lazy=True)
    targets = db.relationship('Target', backref='author', lazy=True)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout = db.Column(db.Text, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout = db.Column(db.Text, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    target = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)