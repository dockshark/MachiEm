import pytest
from src.deep_learning_model import build_deep_learning_model, train_deep_learning_model
import numpy as np

def test_build_deep_learning_model():
    model = build_deep_learning_model(3)
    assert model is not None
    assert len(model.layers) == 4

def test_train_deep_learning_model():
    data = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    labels = np.array([0, 0, 0, 1, 1, 1, 1, 1])
    model = train_deep_learning_model(data, labels)
    assert model is not None
