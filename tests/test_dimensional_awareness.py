import pytest
from src.dimensional_awareness import advanced_quantum_circuit, prepare_ml_data, train_ml_model

def test_advanced_quantum_circuit():
    counts = advanced_quantum_circuit()
    assert isinstance(counts, dict)

def test_prepare_ml_data():
    counts = {"000": 25, "001": 30, "010": 45, "011": 55, "100": 60, "101": 70, "110": 80, "111": 90}
    data, labels = prepare_ml_data(counts)
    assert data.shape[0] == len(labels)

def test_train_ml_model():
    data = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    labels = [0, 0, 0, 1, 1, 1, 1, 1]
    model = train_ml_model(data, labels)
    assert model is not None
