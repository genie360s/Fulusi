import pytest
from flaskr.db import get_db

def test_dashboard_route_requires_login(client):
    response = client.get('/dashboard/dashboard')
    assert response.status_code == 302  # Redirects to login page

def test_dashboard_route_with_authenticated_user(authenticated_client):
    response = authenticated_client.get('/dashboard/dashboard')
    assert response.status_code == 200  # Should return dashboard
