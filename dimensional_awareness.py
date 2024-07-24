from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer

def quantum_circuit_demo():
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])
    qc.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    qobj = assemble(qc)
    result = simulator.run(qobj).result()
    counts = result.get_counts()
    print(counts)
    plot_histogram(counts)

if __name__ == "__main__":
    quantum_circuit_demo()
