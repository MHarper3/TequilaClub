from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tequilas_consumed = db.relationship('Tequila', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"User: {self.username}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Tequila():
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(128), index=True)
    type = db.Column(db.String(64), index=True)
    product_name = db.Column(db.String(120), index=True, unique=True)
    price = db.Column(db.Float)
    comments = db.relationship('Rating', backref='tequila', lazy='dynamic')

    def __repr__(self):
        return f"{self.product_name} by {self.brand}"

class Rating():
    id = db.Column(db.Integer, primary_key=True)
    out_of_5 = db.Column(db.Integer)
    comments = db.Column(db.String(500))


