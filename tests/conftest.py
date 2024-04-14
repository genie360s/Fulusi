# Description: This file contains the fixtures that are used in the tests.| https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    # create and configure a temporary app instance
    # with a temporary database for testing
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    # create the database and load test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

""" 
The auth fixture logs a user in. The login() method returns a response object from 
the client.post() call. The response is not needed in the test, so the method calls.
follow _redirects() to get the redirected response. The follow_redirects() method is
used to test the redirection to the login page. 
"""
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, email='test@example.com', password='admin'):
        return self._client.post(
            'auth/login',
            data={'email': email, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)

# New fixture specifically for dashboard testing
@pytest.fixture
def authenticated_client(client, auth):
    # Log in a test user before each test
    auth.login()
    yield client
    # Log out the test user after each test
    auth.logout()