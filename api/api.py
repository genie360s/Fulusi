
import os
from flask import Flask, jsonify, request
import psycopg


app = Flask(__name__)

def get_db_connection():
    conn = psycopg.connect(
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME")
    )
    return conn

@app.route('/api/v1/dse_stock_prices', methods=['GET'])
def get_data():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM dse_stock_prices;')
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/api/v1/dse_stock_prices/latest_date', methods=['GET'])
def get_entries_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM dse_stock_prices;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]
        
        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM dse_stock_prices
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date,))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# uttamis api latest date data entry
@app.route('/api/v1/uttamis_unit_prices/latest_date', methods=['GET'])
def get_uttamis_entries_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM uttamis_fund;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]
        
        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM uttamis_fund
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date,))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# azania bank api latest date data entry
@app.route('/api/v1/azania_bank/latest_date', methods=['GET'])
def get_azania_bank_latest_forex_rates():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM azania_bank;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]
        
        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM azania_bank
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date,))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

# government bonds latest api
@app.route('/api/v1/government_bonds/latest_date', methods=['GET'])
def get_government_bonds_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM government_bonds;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]

        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM government_bonds
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date, ))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
#corporate bonds latest api
@app.route('/api/v1/corporate_bonds/latest_date', methods=['GET'])
def get_corporate_bonds_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM corporate_bonds;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]

        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM corporate_bonds
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date, ))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

#baroda bank latest api
@app.route('/api/v1/baroda_bank/latest_date', methods=['GET'])
def get_baroda_bank_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM bank_of_baroda;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]

        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM bank_of_baroda
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date, ))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
#bank_of_india latest api
@app.route('/api/v1/bank_of_india/latest_date', methods=['GET'])
def get_bank_of_india_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM bank_of_india;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]

        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM bank_of_india
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date, ))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
#amana bank latest api
@app.route('/api/v1/amana_bank/latest_date', methods=['GET'])
def get_amana_bank_latest_date():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to get the latest date
        cursor.execute('SELECT MAX(DATE(created_at)) FROM amana_bank;')
        latest_date_row = cursor.fetchone()
        latest_date = latest_date_row[0]

        if not latest_date:
            return jsonify({"error": "No data available"}), 404

        # Query to get entries for the latest date
        query = '''
            SELECT * FROM amana_bank
            WHERE DATE(created_at) = %s;
        '''
        cursor.execute(query, (latest_date, ))
        rows = cursor.fetchall()

        if not rows:
            return jsonify({"error": "No data found for the latest date"}), 404

        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, row)) for row in rows]
        cursor.close()
        connection.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
