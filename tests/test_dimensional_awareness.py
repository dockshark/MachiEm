import unittest
from src.dimensional_awareness import advanced_quantum_circuit, prepare_ml_data, train_ml_model

class TestDimensionalAwareness(unittest.TestCase):
    def test_quantum_circuit(self):
        results = advanced_quantum_circuit()
        self.assertIsNotNone(results)

    def test_ml_data_preparation(self):
        results = {'000': 100, '111': 60, '001': 30}
        data, labels = prepare_ml_data(results)
        self.assertEqual(len(data), 3)
        self.assertEqual(len(labels), 3)

    def test_ml_model_training(self):
        results = {'000': 100, '111': 60, '001': 30, '010': 20, '101': 10}
        data, labels = prepare_ml_data(results)
        model = train_ml_model(data, labels)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()