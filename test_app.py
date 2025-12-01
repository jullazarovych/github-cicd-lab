import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_status(client):
    rv = client.get('/status')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['status'] == 'OK'

def test_add(client):
    rv = client.get('/add/5/3')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['result'] == 8