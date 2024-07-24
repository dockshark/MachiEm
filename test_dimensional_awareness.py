from qiskit_aer import Aer
from dimensional_awareness import quantum_circuit_demo

def test_quantum_circuit_demo():
    assert quantum_circuit_demo() is not None
