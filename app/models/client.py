from app import db
from datetime import datetime

class Client(db.Model):
    __tablename__ = 'api_client'
    id = db.Column(db.Integer, primary_key=True)
    direction = db.Column(db.String(80), nullable=False)
    credit_card = db.Column(db.String(16))
    web_page = db.Column(db.String(200))
    pay_mode = db.Column(db.String(10))
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('api_user.id'))
    # Relaciones
    tickets = db.relationship('Ticket', backref='client', lazy=True)
    domains = db.relationship('Domain', backref='client', lazy=True)