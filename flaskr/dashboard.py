#dashboard blue print
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, url_for, request
)
import requests
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from requests.exceptions import Timeout

from dotenv import load_dotenv

load_dotenv()

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
@bp.route('/dashboard', methods=('GET', 'POST'))
@login_required
def dashboard():
    # dashboard logic goes in here
    if request.method == 'POST':
        bank_name = request.form['bank_name']
        print(bank_name)
        error = None

        if not bank_name:
            error = 'Bank name is required.'
        base_api_url = os.getenv("BASE_API_URL")
        bank_api_url = f"{base_api_url}{bank_name}/latest_date"
        if  error is None:
            try :
                response = requests.get(bank_api_url)
                if response.status_code == 200:
                    bank_forex_data = response.json()
                    print(bank_forex_data)
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
        print(fund_name)
        error = None

        if not fund_name:
            error = 'Fund name is required.'

        base_api_url = os.getenv("BASE_API_URL")
        fund_api_url = f"{base_api_url}{fund_name}/latest_date"

        if  error is None:
            try :
                response = requests.get(fund_api_url)
                if response.status_code == 200:
                    fund_data = response.json()
                    print(fund_data)
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

@bp.route('/stock_markets', methods=('GET', 'POST'))
@login_required
def stock_markets():
    #checks which stock market is selected

    if request.method == 'POST':
        stock_market = request.form['stock_market']
        error = None

        if not stock_market:
            error = 'Stock market is required.'

        if  stock_market == "dse":
           
            dse_api = os.getenv("DSE_STOCK_PRICES_API_URL")
            

            try :
                response = requests.get(dse_api,  verify=False)
                print(response.json)
                if response.status_code == 200:
                    stock_data = response.json()
                    stock_data = stock_data['data']
                    print(stock_data)
                    print("DSE")
                    return render_template('dashboard/stock_markets.html', stock_data=stock_data)
          
            except Exception as e:
                # Handle other exceptions
                return render_template('error.html', message=f"Failed to fetch data from the API: {str(e)}")
            else:
                # Handle other errors
                return render_template('error.html', message="Failed to fetch data from the API")
        flash(error)
    return render_template('dashboard/stock_markets.html')

@bp.route('/bonds', methods=('GET', 'POST'))
@login_required
def bonds():
    # bond  logic goes in here
    if request.method == 'POST':
        bond_type = request.form['bond_type']
        print(bond_type)
        error = None

        if not bond_type:
            error = 'Bond type is required.'

        base_api_url = os.getenv("BASE_API_URL")
        bond_api_url = f"{base_api_url}{bond_type}/latest_date"

        if  error is None:
            try :
                response = requests.get(bond_api_url)
                if response.status_code == 200:
                    bond_data = response.json()
                    print(bond_data)
                    return render_template('dashboard/bonds.html', bond_data=bond_data)
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
    return render_template('dashboard/bonds.html')

@bp.route('/best_banks_forex_rates_tz', methods=('GET', 'POST'))
@login_required
def best_banks_forex_rates_tz():
    try:
        response = requests.get(os.getenv("BEST_BANKS_FOREX_RATES_TZ_API_URL"), timeout=10)
        if response.status_code == 200:
            best_banks_forex_rates = response.json()
            print(best_banks_forex_rates)
            return render_template('dashboard/best_banks_forex_rates.html', best_banks_forex_rates=best_banks_forex_rates)
        else:
            return render_template('error.html', message=f"Error fetching data: {response.status_code}")
    except Timeout:
        return render_template('error.html', message="API request timed out. Please try again later.")
    except Exception as e:
        return render_template('error.html', message=f"Failed to fetch data from the API: {str(e)}")
    
    return render_template('dashboard/best_banks_forex_rates.html')

@bp.route('/best_banks_forex_rates_summary', methods=('GET', 'POST'))
@login_required
def banks_summary_forex_rates_tz():
    try:
        response = requests.get(os.getenv("BEST_BANKS_FOREX_RATES_SUMMARY_TZ_API_URL"), timeout=10)
        if response.status_code == 200:
            summary_best_rates = response.json()
            print(summary_best_rates)
            return render_template('dashboard/forex_rates_summary.html', summary_best_rates=summary_best_rates)
        else:
            return render_template('error.html', message=f"Error fetching data: {response.status_code}")
    except Timeout:
        return render_template('error.html', message="API request timed out. Please try again later.")
    except Exception as e:
        return render_template('error.html', message=f"Failed to fetch data from the API: {str(e)}")
    
    return render_template('dashboard/forex_rates_summary.html')
