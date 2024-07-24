from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def advanced_quantum_circuit():
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.ccx(0, 1, 2)
    qc.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    qobj = assemble(qc)
    result = simulator.run(qobj).result()
    counts = result.get_counts()
    print(counts)
    plot_histogram(counts)
    return counts

def prepare_ml_data(counts):
    data = []
    labels = []
    for state, count in counts.items():
        features = [int(bit) for bit in state]
        label = 1 if count > 50 else 0
        data.append(features)
        labels.append(label)
    return np.array(data), np.array(labels)

def train_ml_model(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')
    return model

if __name__ == "__main__":
    results = advanced_quantum_circuit()
    data, labels = prepare_ml_data(results)
    model = train_ml_model(data, labels)