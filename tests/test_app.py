# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the homepage"""
    rv = client.get('/')
    assert rv.data == b'Hello, DevOps World!'
