from pyscf import gto, scf


def create_h2_molecule(bond_length):
    molecule = gto.M(
        atom=f"H 0 0 0; H 0 0 {bond_length}",
        basis="sto-3g",
        unit="Angstrom",
        charge=0,
        spin=0,
        verbose=0,
    )

    return molecule


def run_hartree_fock(bond_length):
    molecule = create_h2_molecule(bond_length)

    calculation = scf.RHF(molecule)
    energy = calculation.kernel()

    return energy
