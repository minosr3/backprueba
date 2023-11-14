from app import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = 'api_invoice'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('api_client.id'))