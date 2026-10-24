from h2_vqe.vqe_solver import calculate_vqe_energy


def test_vqe_energy():
    energy = calculate_vqe_energy(0.74)

    assert energy < 0
    assert energy > -2
