from elements import ATOMIC_MASSES

def calculate_molar_mass(parsed_formula):
    """
    Calculate the molar mass of a chemical formula.
    Parameters:
        parsed_formula (dict): A dictionary which contains element symbols and their counts.
    Returns:
        float: The molar mass in g/mol.
    """

    total_mass = 0.0

    for element , count in parsed_formula.items():
        total_mass += ATOMIC_MASSES[element] * count

    return total_mass
