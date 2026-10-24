
import pandas as pd

from h2_vqe.config import BOND_LENGTHS
from h2_vqe.exact_solver import calculate_exact_energy
from h2_vqe.vqe_solver import calculate_vqe_details


def run_experiment():
    results = []

    for bond_length in BOND_LENGTHS:
        print(f"Calculating bond length: {bond_length:.2f} Angstrom")

        exact_energy = calculate_exact_energy(bond_length)
        vqe_result = calculate_vqe_details(bond_length)

        vqe_energy = vqe_result["energy"]

        results.append({
            "bond_length_angstrom": bond_length,
            "exact_energy_hartree": exact_energy,
            "vqe_energy_hartree": vqe_energy,
            "absolute_error_hartree": abs(vqe_energy - exact_energy),
            "optimizer_evaluations": vqe_result["evaluations"],
            "reached_evaluation_limit": vqe_result[
                "reached_evaluation_limit"
            ],
            "optimizer_message": vqe_result["optimizer_message"],
        })

    dataframe = pd.DataFrame(results)
    dataframe.to_csv("results/h2_vqe_results.csv", index=False)

    print("\nExperiment completed.")
    print("Results saved to results/h2_vqe_results.csv")
    print("Geometries calculated:", len(dataframe))
    print(
        "Maximum absolute error:",
        dataframe["absolute_error_hartree"].max(),
        "Hartree",
    )
    print("\nEvaluation-limit diagnostic:")
    print(dataframe["reached_evaluation_limit"].value_counts())


if __name__ == "__main__":
    run_experiment()
