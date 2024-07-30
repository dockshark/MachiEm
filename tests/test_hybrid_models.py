import pytest
from src.hybrid_models import hybrid_model
import numpy as np

def test_hybrid_model():
    data = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
    labels = np.array([0, 0, 0, 1, 1, 1, 1, 1])
    model = hybrid_model(data, labels)
    assert model is not None
