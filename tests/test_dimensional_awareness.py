import unittest
import sys
import os

# Add src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from dimensional_awareness import advanced_quantum_circuit, prepare_ml_data, train_ml_model

class TestDimensionalAwareness(unittest.TestCase):
    def test_quantum_circuit(self):
        results = advanced_quantum_circuit()
        self.assertIsNotNone(results)

    def test_ml_data_preparation(self):
        results = {'000': 100, '111': 60, '001': 30}
        data, labels = prepare_ml_data(results)
        self.assertEqual(len(data), 3)
        self.assertEqual
