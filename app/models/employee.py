from app import db
from datetime import datetime

class Employee(db.Model):
    __tablename__ = 'api_employee'
    id = db.Column(db.Integer, primary_key=True)
    hire_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('api_user.id'))