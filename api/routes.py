from flask import current_app as app, request, jsonify, Blueprint
from . import db
from .models import DseStockPrices

api = Blueprint('api', __name__)

# @todo: add necessary routes

@api.route('/dse_stock_prices', methods=['GET'])
def get_dse_stock_prices():
    dse_stock_prices = DseStockPrices.query.all()
    return jsonify([stock.to_dict() for stock in dse_stock_prices])