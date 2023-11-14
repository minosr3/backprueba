from app import db
from datetime import datetime

class Distributor(db.Model):
    __tablename__ = 'api_distributor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(10))
    client_id = db.Column(db.Integer, db.ForeignKey('api_client.id'))