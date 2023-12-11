from . import db
from flask_login import UserMixin
"""Models for Flask app."""

class Booking(db.Model):
    """Booking model."""
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(5), nullable=False)
    end_time = db.Column(db.String(5), nullable=False)
    reserved_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    bookings = db.relationship('Booking')
