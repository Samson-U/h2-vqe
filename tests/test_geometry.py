from h2_vqe.config import BOND_LENGTHS, NUM_GEOMETRIES
from h2_vqe.molecule import create_h2_molecule, run_hartree_fock


def test_number_of_geometries():
    assert NUM_GEOMETRIES == 43


def test_first_bond_length():
    assert BOND_LENGTHS[0] == 0.40


def test_last_bond_length():
    assert BOND_LENGTHS[-1] == 2.50


def test_bond_length_spacing():
    for i in range(len(BOND_LENGTHS) - 1):
        difference = round(BOND_LENGTHS[i + 1] - BOND_LENGTHS[i], 2)
        assert difference == 0.05


def test_h2_molecule():
    molecule = create_h2_molecule(0.74)
    assert molecule.nelectron == 2


def test_hartree_fock():
    energy = run_hartree_fock(0.74)
    assert energy < 0
