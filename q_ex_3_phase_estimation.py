from qiskit.algorithms import PhaseEstimation
from qiskit.test.mock import FakeSantiago
from qiskit import QuantumCircuit
santiago = FakeSantiago()

# We will first define the problem:
# Our unitary (Q) will be the T gate
unitary = QuantumCircuit(1)
unitary.t(0)

# Our state (|psi>) will be |1>
state_prep = QuantumCircuit(1)
state_prep.x(0)

# Construct our algorithm instance. We will use
# a simulated Santiago device, and three
# evaluation qubits
phase_estimator = PhaseEstimation(3, santiago)

# Next, run this algorithm on our input problem
result = phase_estimator.estimate(unitary,
                                  state_prep)

# Finally, access the result
result.phase  # Has value: 0.125
