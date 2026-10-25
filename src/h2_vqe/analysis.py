import pandas as pd

from h2_vqe.utils import RESULTS_DIR


RESULTS_FILE = RESULTS_DIR / "h2_vqe_results.csv"


def load_results(path=RESULTS_FILE):
    """Load the VQE experiment results from a CSV file."""
    path = RESULTS_FILE if path is None else path
    dataframe = pd.read_csv(path)

    required_columns = {
        "bond_length_angstrom",
        "exact_energy_hartree",
        "vqe_energy_hartree",
        "absolute_error_hartree",
    }

    missing = required_columns.difference(dataframe.columns)

    if missing:
        raise ValueError(
            f"Results file is missing required columns: {sorted(missing)}"
        )

    if dataframe.empty:
        raise ValueError("The results file contains no data.")

    return dataframe


def summarize_results(dataframe):
    """Calculate basic statistics for the VQE experiment."""
    errors = dataframe["absolute_error_hartree"]

    minimum_row = dataframe.loc[
        dataframe["exact_energy_hartree"].idxmin()
    ]

    return {
        "number_of_geometries": len(dataframe),
        "maximum_absolute_error_hartree": float(errors.max()),
        "mean_absolute_error_hartree": float(errors.mean()),
        "minimum_absolute_error_hartree": float(errors.min()),
        "minimum_exact_energy_hartree": float(
            minimum_row["exact_energy_hartree"]
        ),
        "bond_length_at_grid_minimum_angstrom": float(
            minimum_row["bond_length_angstrom"]
        ),
    }


def main():
    dataframe = load_results()
    summary = summarize_results(dataframe)

    print("H2 VQE Experiment Summary")
    print("=" * 28)

    for name, value in summary.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
