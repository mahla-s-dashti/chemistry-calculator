def parse_formula(formula):
    result = {}
    i = 0
    length = len(formula)

    while i < length:

        # Read element symbol
        if formula[i].isupper():
            element = formula[i]
            i += 1

            # Check for a lowercase letter
            if i < length and formula[i].islower():
                element += formula[i]
                i += 1

            # Read element count
            count = 1

            if i < length and formula[i].isdigit():
                num_str = ""

                while i < length and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1

                count = int(num_str)

            # Store element and count
            if element in result:
                result[element] += count
            else:
                result[element] = count

        else:
            raise ValueError(
                f"Unexpected character '{formula[i]}' at position {i}"
            )

    return result
