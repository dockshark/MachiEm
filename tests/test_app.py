import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome to MachiEm' in rv.data

def test_run_circuit(client):
    rv = client.post('/run_circuit', json={})
    assert rv.status_code == 200
    assert isinstance(rv.json, dict)

def test_prepare_ml_data(client):
    rv = client.post('/prepare_ml_data', json={
        "counts": {
            "000": 25, "001": 30, "010": 45, "011": 55,
            "100": 60, "101": 70, "110": 80, "111": 90
        }
    })
    assert rv.status_code == 200
    assert 'data' in rv.json
    assert 'labels' in rv.json

def test_train_ml_model(client):
    rv = client.post('/train_ml_model', json={
        "data": [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
        "labels": [0, 0, 0, 1, 1, 1, 1, 1]
    })
    assert rv.status_code == 200
    assert rv.json['status'] == 'Logistic Regression Model trained successfully'

def test_train_deep_learning_model(client):
    rv = client.post('/train_deep_learning_model', json={
        "data": [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
        "labels": [0, 0, 0, 1, 1, 1, 1, 1]
    })
    assert rv.status_code == 200
    assert rv.json['status'] == 'Deep Learning Model trained successfully'
