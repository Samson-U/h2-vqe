from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.units import DistanceUnit


def build_hamiltonian(bond_length):
    driver = PySCFDriver(
        atom=f"H 0 0 0; H 0 0 {bond_length}",
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )

    problem = driver.run()

    # Build the electronic Hamiltonian
    second_q_op = problem.hamiltonian.second_q_op()

    # Convert it into a qubit Hamiltonian
    mapper = JordanWignerMapper()
    qubit_hamiltonian = mapper.map(second_q_op)

    # Nuclear repulsion energy is kept separate
    nuclear_energy = problem.hamiltonian.nuclear_repulsion_energy

    return qubit_hamiltonian, nuclear_energy
