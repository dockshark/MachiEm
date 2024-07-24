from dimensional_awareness import quantum_circuit_demo

def test_quantum_circuit_demo():
    counts = quantum_circuit_demo()
    assert counts is not None
    assert isinstance(counts, dict)
