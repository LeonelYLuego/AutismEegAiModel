from flask import Blueprint

ai_blueprint = Blueprint('ai', __name__)

from . import routes