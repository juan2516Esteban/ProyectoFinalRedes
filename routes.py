# my_flask_app/app/routes.py

from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Hello, World!'
