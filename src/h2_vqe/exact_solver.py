import numpy as np
from scipy.linalg import eigh

from h2_vqe.hamiltonian import build_hamiltonian


def calculate_exact_energy(bond_length):
    operator, nuclear_energy = build_hamiltonian(bond_length)

    # Convert the qubit Hamiltonian to a matrix
    matrix = operator.to_matrix()

    # Find all eigenvalues
    eigenvalues = eigh(matrix, eigvals_only=True)

    # Lowest eigenvalue is the ground-state electronic energy
    electronic_energy = eigenvalues[0]

    # Add nuclear repulsion once
    total_energy = electronic_energy + nuclear_energy

    return total_energy
