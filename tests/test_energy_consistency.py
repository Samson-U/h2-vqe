from h2_vqe.exact_solver import calculate_exact_energy


def test_exact_energy():
    energy = calculate_exact_energy(0.74)

    assert energy < 0
    assert energy > -2
