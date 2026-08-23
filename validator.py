from elements import  ATOMIC_MASSES 

def validate_formula(parsed_formula):
    """
    validate that all elements in the parsed formula 
    exist in the atomic mass table .
    """
    unknown_elements = []

    for element in parsed_formula:
        if element not in ATOMIC_MASSES:

unknown_elements.append(element)

    if unknown_elements:
        raise ValueError(f"Unknown element(s):{' , '.join(unknown_elements)}")
    return True
