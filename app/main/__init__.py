from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .config import config_by_name
db = SQLAlchemy()

def create_app(config_name):
    app = Flask('AutismAI')
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    db.init_app(app)

    with app.app_context():
        from .ai import ai_blueprint
        app.register_blueprint(ai_blueprint, url_prefix='/api')
        return app