import os
import secrets
# Generate a secure random secret key of length 32 characters

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
