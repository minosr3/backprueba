from flask import Flask
from app.api.tickets import tickets_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.ConfigClass')

db = SQLAlchemy(app)

app.register_blueprint(tickets_bp, url_prefix='/api')
