from typing import Any
import pytest
from flask import Flask, g, session
from flaskr.db import get_db


def test_register(client: Any, app: Flask):
    assert client.get('/auth/register').status_code == 200
    # The client.post() method sends a POST request to the server. | registering the user
    response = client.post('/auth/register', data={'fullname' : 'Test User','username' : 'a','email': 'a@example.com', 'password': 'admin', 'terms_and_conditions': 'True'})
    assert response.headers['Location'] == '/auth/login'

    with app.app_context():
        assert get_db().execute(
            "SELECT * from user where username = 'a'",
        ).fetchone() is not None

@pytest.mark.parametrize(( 'fullname', 'username', 'email', 'password', 'terms_and_conditions', 'message'), (
    ('', '', '', '', '', b'required'),
    ('Test User', '', '', '', '', b'required'),
    ('Test User', 'a', '', '', '', b'required'),
    ('Test User', 'a', 'a@example.com', '', '', b'required'),
    ('Test User', 'a', 'a@example.com', 'admin', '', b''),
    ('Test User', 'test', 'test@example.com', 'admin', 'True', b''),
))

def test_register_validate_input(client: Any, username: str, fullname: str, email: str, password: str, terms_and_conditions: str, message: bytes):
    response = client.post(
        '/auth/register', 
        data={'fullname': fullname, 'username': username, 'email': email, 'password': password, 'terms_and_conditions': terms_and_conditions})
    assert message in response.data

def test_login(client: Any, auth: Any):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == '/dashboard/dashboard'

    with client:
        client.get('dashboard/dashboard')
        assert session['user_id'] == 1
        assert g.user['email'] == 'test@example.com'

@pytest.mark.parametrize(('email', 'password', 'message'), (
    ('test@example.com', 'password', b''),
    ('password', 'test@example.com', b''),
))
def test_login_validate_input(auth: Any, email: str, password: str, message: bytes):
    response = auth.login(email, password)
    assert message in response.data

def test_logout(client: Any, auth: Any):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session