# config.py

class Config(object):
    SECRET_KEY = 'tu_clave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tickets.db'  # O tu URL de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
