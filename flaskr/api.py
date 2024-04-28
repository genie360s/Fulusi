#api blue print
from flask import (
    Blueprint, Flask, jsonify, request
)

# from werkzeug.exceptions import abort
# from flaskr.auth import login_required
# from flaskr.db import get_db
import os
import json



bp = Blueprint('api', __name__, url_prefix='/findaily')
@bp.route('/api/<file_name>')

def get_data(file_name):
    #navigate to the data folder
    finscrap_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'finscrap'))
    file_path = os.path.join(finscrap_dir, 'data', f'{file_name}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data) if data else jsonify({'error': 'Data not found'})
    else:
        return jsonify({'error': 'Data not found'}), 404@bp.route('/api', methods=['POST'])
    
@bp.route('/api/bot', methods=['POST']) 
def post_data():
    
    filename = "bot"
    # Navigate up two levels to reach the "finscrap" directory
    finscrap_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'finscrap'))

    # Construct the file path relative to the "finscrap/data" folder
    file_path = os.path.join(finscrap_dir,  'data', f'{filename}.json')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({'error': 'Data not found'}), 404
