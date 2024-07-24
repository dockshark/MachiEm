from qiskit import QuantumCircuit, Aer, transpile, assemble

def quantum_circuit_demo():
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])
    qc.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    qobj = assemble(qc)
    result = simulator.run(qobj).result()
    counts = result.get_counts()
    print(counts)
