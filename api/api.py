
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

if __name__ == '__main__':
    app.run(debug=True)
