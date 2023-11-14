from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'api_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    document = db.Column(db.String(100))
    document_type = db.Column(db.String(30))
    # Relaciones
    clients = db.relationship('Client', backref='user', lazy=True)
    employees = db.relationship('Employee', backref='user', lazy=True)