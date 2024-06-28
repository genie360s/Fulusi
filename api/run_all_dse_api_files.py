import subprocess

# List of Python files you want to run
files_to_run = ['dse_gainers_losers.py', 'dse_latest_trading_indices.py', 'dse_market_overview.py', 'dse_stock_prices.py']

# Iterate over the list and run each file
for file in files_to_run:
    subprocess.call(['python3', file])