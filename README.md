
# H₂ Potential Energy Curve Using the Variational Quantum Eigensolver

**A reproducible quantum chemistry project using Qiskit, Qiskit Nature, and PySCF**

---

## 1. Overview

How does the energy of a hydrogen molecule change as the distance between its two nuclei increases?

This project investigates that question by calculating the potential energy curve of molecular hydrogen (H₂) using the **Variational Quantum Eigensolver (VQE)** and comparing its energies against an exact diagonalization reference.

The experiment evaluates 43 internuclear distances from 0.40 Å to 2.50 Å, using a spacing of 0.05 Å and the STO-3G minimal basis set. PySCF and Qiskit Nature provide the molecular electronic structure workflow, while Qiskit Algorithms implements VQE.

The project is designed as a laptop-based, reproducible introduction to quantum algorithms for molecular energy estimation.

## 2. Scientific Objectives

- Construct the electronic Hamiltonian of neutral H₂ at different internuclear distances.
- Map the fermionic Hamiltonian to qubits using the Jordan–Wigner transformation.
- Estimate molecular energies using VQE with a Hartree–Fock reference state and UCCSD ansatz.
- Compare VQE energies with an exact diagonalization reference.
- Analyze the absolute energy error across the bond-length range.
- Identify the minimum-energy geometry on the sampled grid.
- Generate numerical results, plots, and automated tests.
- Validate the reference-energy implementation independently across the full grid.

## 3. Methodology

| Component | Configuration |
|---|---|
| Molecule | Neutral H₂ |
| Total charge | 0 |
| Spin | Singlet; PySCF spin parameter 0 |
| Basis set | STO-3G |
| Bond-length range | 0.40–2.50 Å |
| Grid spacing | 0.05 Å |
| Number of geometries | 43 |
| Fermion-to-qubit mapping | Jordan–Wigner |
| VQE ansatz | Unitary Coupled Cluster Singles and Doubles (UCCSD) |
| Reference state | Hartree–Fock |
| Classical optimizer | COBYLA |
| Optimizer limit | `maxiter=1000` |
| Simulation | Statevector-based evaluation |
| Reference calculation | Exact diagonalization of the mapped qubit Hamiltonian |

The reported total energy includes the electronic energy and nuclear repulsion energy, with nuclear repulsion added exactly once.

The exact solver diagonalizes the mapped qubit Hamiltonian. Its results were independently checked against Qiskit Nature's `GroundStateEigensolver` with `NumPyMinimumEigensolver` at all 43 sampled geometries.

## 4. Technology Stack

- **Python 3.12** — primary programming language
- **Qiskit** — quantum circuits and primitives
- **Qiskit Nature** — molecular Hamiltonians and chemistry workflows
- **Qiskit Algorithms** — VQE and classical optimization
- **PySCF** — molecular electronic structure calculations
- **NumPy and SciPy** — numerical operations and linear algebra
- **Pandas** — result storage and analysis
- **Matplotlib** — scientific plots
- **Pytest** — automated testing

## 5. Project Structure

```text
h2-vqe-project/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── docs/
│   └── main_project_document.docx
├── src/
│   └── h2_vqe/
│       ├── __init__.py
│       ├── config.py
│       ├── molecule.py
│       ├── hamiltonian.py
│       ├── exact_solver.py
│       ├── vqe_solver.py
│       ├── run_experiment.py
│       ├── analysis.py
│       ├── plotting.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_geometry.py
│   ├── test_hamiltonian.py
│   ├── test_energy_consistency.py
│   └── test_results.py
├── data/
│   └── raw/
└── results/
    ├── h2_vqe_results.csv
    ├── energy_curve.png
    └── error_curve.png
```

## 6. Getting Started

### 6.1 Activate the environment

From the project root:

```bash
source .venv/bin/activate
```

### 6.2 Check dependencies

```bash
python -m pip check
```

### 6.3 Run automated tests

```bash
PYTHONPATH=src python -m pytest -q
```

The latest test run passed all 9 tests. Qiskit deprecation warnings and SciPy sparse-matrix efficiency warnings were present, but they did not cause test failures.

### 6.4 Run the full experiment

```bash
PYTHONPATH=src python -m h2_vqe.run_experiment
```

This recalculates the exact reference and VQE energies at every configured bond length and writes the results to `results/h2_vqe_results.csv`.

### 6.5 Generate plots

```bash
PYTHONPATH=src python -m h2_vqe.plotting
```

The plotting script generates the energy comparison and absolute-error figures.

## 7. Results

The latest recorded experiment produced the following results:

| Metric | Result |
|---|---:|
| Geometries evaluated | 43 |
| Bond-length range | 0.40–2.50 Å |
| Grid spacing | 0.05 Å |
| Minimum exact total energy on the grid | −1.1371170673 Hartree |
| Bond length at the grid minimum | 0.75 Å |
| Maximum absolute VQE–reference energy difference | 5.9097 × 10⁻⁷ Hartree |
| Optimizer evaluations across geometries | 40–280 |
| Automated tests passed | 9 of 9 |
| Missing CSV values | 0 |
| Independent reference geometries checked | 43 |
| Maximum difference between exact solvers | 4.44 × 10⁻¹⁵ Hartree |

These values describe the latest recorded run. Recalculate and update them if the configuration, software, or implementation changes.

### 7.1 Generated outputs

**`results/h2_vqe_results.csv`**

Contains one row per geometry with:

- `bond_length_angstrom`: internuclear distance in angstroms
- `exact_energy_hartree`: reference total energy in Hartree
- `vqe_energy_hartree`: VQE total energy in Hartree
- `absolute_error_hartree`: absolute VQE–reference difference
- `optimizer_evaluations`: number of objective-function evaluations reported by VQE
- `reached_evaluation_limit`: diagnostic indicating whether the reported evaluation count reached the configured numeric limit
- `optimizer_message`: explanation of the diagnostic status

**`results/energy_curve.png`**

Compares VQE and reference energies across the sampled bond lengths.

**`results/error_curve.png`**

Shows the absolute difference between VQE and reference energies across the sampled bond lengths.

## 8. Interpretation

The lowest exact total energy among the 43 sampled geometries occurs at 0.75 Å. This is the **minimum on the specified discrete grid**, not the result of a continuous optimization of the equilibrium bond length.

The VQE energies closely track the reference values in the latest experiment. The maximum absolute difference is approximately 5.91 × 10⁻⁷ Hartree.

The independent reference check found a maximum difference of approximately 4.44 × 10⁻¹⁵ Hartree between the project's exact solver and Qiskit Nature's ground-state solver across all 43 geometries. This supports the consistency of the exact-energy calculation for the implemented setup.

## 9. Validation and Limitations

### 9.1 Completed checks

- All 43 configured bond lengths were evaluated.
- The results CSV contains 43 rows and no missing values.
- The automated test suite passed all 9 tests.
- The exact-energy solver was independently compared with Qiskit Nature's ground-state solver at all 43 geometries.
- The maximum difference between those two reference calculations was approximately 4.44 × 10⁻¹⁵ Hartree.
- The energy convention includes nuclear repulsion exactly once.

### 9.2 Optimizer convergence reporting

The installed Qiskit `OptimizerResult` exposes optimized parameters, objective value, and evaluation count, but does not expose SciPy's `success` or `message` fields through this interface.

Therefore, the current CSV does **not** claim formal optimizer convergence. `reached_evaluation_limit` is only a diagnostic based on the evaluation count; stopping before the configured limit does not prove convergence or establish that a global minimum was found.

The small VQE–reference energy differences are encouraging evidence of numerical agreement, but they do not replace a formal convergence analysis.

### 9.3 Scientific limitations

- **Minimal basis set:** STO-3G is computationally economical but limits the flexibility of the electronic wavefunction.
- **Ideal simulation:** The calculations do not include hardware noise, finite-shot measurement uncertainty, or hardware connectivity constraints.
- **Optimization:** VQE performance depends on the ansatz, initial parameters, and optimizer behavior.
- **Reference scope:** The independent solver agreement validates the reference calculation for this implemented setup; it does not establish the accuracy of the STO-3G model relative to experiment.
- **Grid resolution:** The equilibrium geometry is identified only among the sampled distances.
- **Software warnings:** Current dependencies produce deprecation and sparse-matrix efficiency warnings. They did not prevent the tested calculations from completing.

Passing automated tests demonstrates that the implemented test cases succeed. It does not, by itself, prove every scientific assumption or guarantee optimizer convergence.

## 10. Reproducibility

To reproduce the experiment:

1. Use a compatible Python environment.
2. Activate the project's virtual environment.
3. Install the dependencies specified by the project.
4. Run `python -m pip check`.
5. Run the automated tests.
6. Execute the full experiment.
7. Regenerate the plots.
8. Inspect the CSV for missing values and unexpected errors.
9. Preserve the source code, dependency versions, configuration, and generated results together.

For a formal release, record the exact installed package versions and any changes to the ansatz, optimizer settings, or energy calculations.

## 11. Future Improvements

- Implement a reliable optimizer-convergence assessment using the optimizer's actual stopping information.
- Record convergence diagnostics and stopping reasons in the results file.
- Add stronger automated checks for VQE accuracy and physical constraints.
- Analyze the potential energy minimum using a justified interpolation or continuous optimization method.
- Compare alternative ansätze and optimizer settings.
- Investigate larger basis sets and more demanding molecular systems.
- Explore noisy simulation or quantum hardware when appropriate.

## 12. Conclusion

This project implements a reproducible workflow for studying molecular hydrogen with VQE. It combines molecular electronic structure calculations, qubit Hamiltonian construction, variational optimization, exact-reference comparison, automated tests, and scientific visualization.

The latest run shows close numerical agreement between VQE and the validated reference-energy curve across the sampled geometries. The exact solver has been independently checked over the complete grid. Formal optimizer-convergence reporting remains a documented improvement before the results should be presented as a fully convergence-validated VQE benchmark.
