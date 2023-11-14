from app import db
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = 'api_ticket'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    state = db.Column(db.String(10), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('api_client.id'))
    Ticket.to_dict = to_dict