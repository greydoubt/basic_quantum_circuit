
# oracle for boolean expressions
from qiskit.circuit.library import PhaseOracle
oracle = PhaseOracle(
        '(A | B)'    # A must go if B doesn't
        '& ~(A & B & C)'  # Can't all go
        '& (B & C)'  # C wants to go with B
	)
