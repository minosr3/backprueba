from app import db
from datetime import datetime

class Domain(db.Model):
    __tablename__ = 'api_domain'
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('api_client.id'))