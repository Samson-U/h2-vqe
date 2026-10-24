import pandas as pd

from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit_algorithms import NumPyMinimumEigensolver

from h2_vqe.exact_solver import calculate_exact_energy


data = pd.read_csv("results/h2_vqe_results.csv")

mapper = JordanWignerMapper()
solver = GroundStateEigensolver(
    mapper,
    NumPyMinimumEigensolver()
)

differences = []

for bond_length in data["bond_length_angstrom"]:
    driver = PySCFDriver(
        atom=f"H 0 0 0; H 0 0 {bond_length}",
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )

    problem = driver.run()
    reference_result = solver.solve(problem)

    reference_energy = float(reference_result.total_energies[0].real)
    project_energy = calculate_exact_energy(bond_length)

    difference = abs(reference_energy - project_energy)
    differences.append(difference)

print("Geometries checked:", len(differences))
print("Maximum reference difference:", max(differences), "Hartree")
print("All differences below 1e-8 Hartree:", max(differences) < 1e-8)
