from parser import parse_formula
from validator import validate_formula
from calculator import calculate_molar_mass


running = True

while running:

    print("=" * 40)
    print("      Chemistry Calculator")
    print("=" * 40)

    print("1. Calculate Molar Mass")
    print("2. Gram → Mole")
    print("3. Mole → Gram")
    print("4. Percent Composition")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ").strip()

    if choice == "1":

        formula = input("\nEnter chemical formula: ").strip()
        formula = formula.replace(" ", "")

        try:

            parsed = parse_formula(formula)

            validate_formula(parsed)

            molar_mass = calculate_molar_mass(parsed)

            print("\nResult")
            print("-" * 30)
            print(f"Formula      : {formula}")
            print(f"Composition  : {parsed}")
            print(f"Molar Mass   : {molar_mass:.3f} g/mol")

        except ValueError as error:
            print(f"\nError: {error}")

    elif choice == "2":
        print("\nThis feature will be added in Version 2.")

    elif choice == "3":
        print("\nThis feature will be added in Version 2.")

    elif choice == "4":
        print("\nThis feature will be added in Version 3.")

    elif choice == "5":
        print("\nThank you for using Chemistry Calculator!")
        running = False

    else:
        print("\nInvalid option.")
