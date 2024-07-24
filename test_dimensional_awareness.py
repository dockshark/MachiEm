# test_dimensional_awareness.py

from dimensional_awareness import quantum_circuit_demo

def test_quantum_circuit_demo():
    try:
        quantum_circuit_demo()
        assert True
    except Exception as e:
        assert False, f"quantum_circuit_demo failed with exception {e}"

# Add more tests here
def test_another_feature():
    # Example test for another feature
    assert True
