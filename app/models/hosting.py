from app import db
from datetime import datetime

class Hosting(db.Model):
    __tablename__ = 'api_hosting'
    id = db.Column(db.Integer, primary_key=True)
    hosting_name = db.Column(db.String(50), nullable=False)
    is_free = db.Column(db.Boolean)
    client_id = db.Column(db.Integer, db.ForeignKey('api_client.id'))