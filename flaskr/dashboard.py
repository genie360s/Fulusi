#dashboard blue print
from flask import (
    Blueprint, flash, g, redirect, render_template, url_for, request
)
import requests
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from requests.exceptions import Timeout
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
@bp.route('/dashboard', methods=('GET', 'POST'))
@login_required
def dashboard():
    # dashboard logic goes in here
    if request.method == 'POST':
        bank_name = request.form['bank_name']
        error = None

        if not bank_name:
            error = 'Bank name is required.'

        api_url = f"https://a68f-197-250-198-20.ngrok-free.app/findaily/api/{bank_name}"
        if  error is None:
            try :
                response = requests.get(api_url)
                if response.status_code == 200:
                    bank_forex_data = response.json()
                    return render_template('dashboard/dashboard.html', bank_forex_data=bank_forex_data)
            except Timeout:
                # Handle timeout error
                return render_template('error.html', message="API request timed out. Please try again later.")
            except Exception as e:
                # Handle other exceptions
                return render_template('error.html', message=f"Failed to fetch data from the API: {str(e)}")
            else:
                # Handle other errors
                return render_template('error.html', message="Failed to fetch data from the API")
            
        flash(error)

    return render_template('dashboard/dashboard.html')


@bp.route('/mutual_funds', methods=('GET', 'POST'))
@login_required
def mutual_funds():
    # mutual funds logic goes in here
    if request.method == 'POST':
        fund_name = request.form['fund_name']
        error = None

        if not fund_name:
            error = 'Fund name is required.'

        api_url = f"https://a68f-197-250-198-20.ngrok-free.app/findaily/api/{fund_name}"
        if  error is None:
            try :
                response = requests.get(api_url)
                if response.status_code == 200:
                    fund_data = response.json()
                    return render_template('dashboard/mutual_funds.html', fund_data=fund_data)
            except Timeout:
                # Handle timeout error
                return render_template('error.html', message="API request timed out. Please try again later.")
            except Exception as e:
                # Handle other exceptions
                return render_template('error.html', message=f"Failed to fetch data from the API: {str(e)}")
            else:
                # Handle other errors
                return render_template('error.html', message="Failed to fetch data from the API")
            
        flash(error)

    return render_template('dashboard/mutual_funds.html')