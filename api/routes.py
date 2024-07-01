from flask import request, jsonify, Blueprint
from . import db
from .models import User

api = Blueprint('api', __name__)

# @todo: add necessary routes