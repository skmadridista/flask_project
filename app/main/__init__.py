# app/main/__init__.py
from flask import Blueprint,url_for


main_bp = Blueprint('main', __name__)

auth_bp = Blueprint('auth',__name__)

# Import routes after creating the blueprint to avoid circular imports
from app.main import routes
# from app import app

