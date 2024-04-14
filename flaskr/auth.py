# documentation for this file | https://flask.palletsprojects.com/en/3.0.x/tutorial/views/
#authentication blueprint
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

#views
#account register view
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        terms_and_conditions = request.form['terms_and_conditions']
        db = get_db()
        error = None

        if not fullname:
            error = 'Fullname is required.'
        elif not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif not terms_and_conditions:
            error = 'You must agree to the terms and conditions.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (fullname, username, email, password, terms_and_conditions) VALUES (?, ?, ?, ?, ?)",
                    (fullname, username, email, generate_password_hash(password), terms_and_conditions),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

#account login view
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
        ).fetchone()
        

        if user is None:
            error = 'Incorrect email address.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            print("yes")
            print(session['user_id'])
            return redirect(url_for('dashboard.dashboard'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

#login decorator | won't allow a user to access a view if they are not logged in
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view