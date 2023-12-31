from app.extensions import db
from flask_login import UserMixin
from .workout import *


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workouts = db.relationship('Workout',backref='author', lazy= True)
    

    def __repr__(self):
        return f'<User {self.name}>'
    


   