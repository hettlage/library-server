from flask import Blueprint

api_v1 = Blueprint('api', __name__)

from . import routes, errors