
import numpy as np

from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorEstimator

from qiskit_nature.second_q.circuit.library import HartreeFock, UCCSD
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.units import DistanceUnit

from h2_vqe.hamiltonian import build_hamiltonian


def calculate_vqe_details(bond_length):
    operator, nuclear_energy = build_hamiltonian(bond_length)
    mapper = JordanWignerMapper()

    driver = PySCFDriver(
        atom=f"H 0 0 0; H 0 0 {bond_length}",
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )
    problem = driver.run()

    hf_state = HartreeFock(
        problem.num_spatial_orbitals,
        problem.num_particles,
        mapper,
    )

    ansatz = UCCSD(
        problem.num_spatial_orbitals,
        problem.num_particles,
        mapper,
        initial_state=hf_state,
    )

    max_evaluations = 1000
    optimizer = COBYLA(maxiter=max_evaluations)

    vqe = VQE(
        StatevectorEstimator(),
        ansatz,
        optimizer,
        initial_point=np.zeros(ansatz.num_parameters),
    )

    result = vqe.compute_minimum_eigenvalue(operator)

    total_energy = float(result.eigenvalue.real + nuclear_energy)
    evaluations = int(result.cost_function_evals)

    # This is a diagnostic, not proof of convergence.
    reached_limit = evaluations >= max_evaluations

    return {
        "energy": total_energy,
        "evaluations": evaluations,
        "reached_evaluation_limit": reached_limit,
        "optimizer_message": (
            "Evaluation limit reached"
            if reached_limit
            else "Stopped before evaluation limit; success not independently verified"
        ),
    }


def calculate_vqe_energy(bond_length):
    # Preserve the numeric return value used by existing tests.
    return calculate_vqe_details(bond_length)["energy"]
