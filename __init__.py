# my_flask_app/app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
