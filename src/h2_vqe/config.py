# H2 VQE project settings

MOLECULE = "H2"
BASIS = "sto-3g"
MAPPING = "Jordan-Wigner"

START_BOND_LENGTH = 0.40
END_BOND_LENGTH = 2.50
BOND_LENGTH_STEP = 0.05

BOND_LENGTHS = [
    round(i / 100, 2)
    for i in range(40, 251, 5)
]

NUM_GEOMETRIES = len(BOND_LENGTHS)
