from h2_vqe.hamiltonian import build_hamiltonian


def test_hamiltonian():
    operator, nuclear_energy = build_hamiltonian(0.74)

    assert operator.num_qubits > 0
    assert len(operator) > 0
    assert nuclear_energy > 0
