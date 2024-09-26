from qiskit import QuantumCircuit
from qiskit.circuit.library import (PhaseOracle,
                                    GroverOperator)
from qiskit.algorithms import EstimationProblem
oracle = PhaseOracle('(A | B) & ~(A & B & C)'
                     '& (B & C)')

grover_op = GroverOperator(oracle)

# Create state preparation operator
n = oracle.num_qubits
state_prep = QuantumCircuit(n)
state_prep.h(range(n))

problem = EstimationProblem(state_prep,
                            [*range(n)],
                      grover_operator=grover_op)
