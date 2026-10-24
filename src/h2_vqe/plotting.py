import pandas as pd
import matplotlib.pyplot as plt


def create_plots():
    data = pd.read_csv("results/h2_vqe_results.csv")

    # Plot the energy curve
    plt.figure()
    plt.plot(
        data["bond_length_angstrom"],
        data["exact_energy_hartree"],
        label="Exact",
        marker="o",
    )
    plt.plot(
        data["bond_length_angstrom"],
        data["vqe_energy_hartree"],
        label="VQE",
        marker="x",
    )

    plt.xlabel("Bond length (Angstrom)")
    plt.ylabel("Energy (Hartree)")
    plt.title("H2 Potential Energy Curve")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/energy_curve.png", dpi=300)
    plt.close()

    # Plot the absolute error
    plt.figure()
    plt.plot(
        data["bond_length_angstrom"],
        data["absolute_error_hartree"],
        marker="o",
    )

    plt.xlabel("Bond length (Angstrom)")
    plt.ylabel("Absolute error (Hartree)")
    plt.title("VQE Error Curve")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/error_curve.png", dpi=300)
    plt.close()

    print("Plots saved in the results folder.")


if __name__ == "__main__":
    create_plots()
