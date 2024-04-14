#dashboard blue print
from flask import (
    Blueprint, flash, g, redirect, render_template, url_for
)

from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
@bp.route('/dashboard')
@login_required
def dashboard():
    # dashboard logic goes in here
    return render_template('dashboard/dashboard.html')