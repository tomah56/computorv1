import argparse
from computor import computor, validate_input

def main(debug):
    try:
        print("\n     ***     Welcome to computor!   ***     \n")
        print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
        if debug:
            print("Debug mode! no user imput.")
            equation_input = "1 * X^0 + 2 * X^1 - 1 * X^2 = 0"
            equation_input = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0" # high degree
            equation_input = "5 * X^0 + 4 * X^1 = 4 * X^0" # irreducible fraction
            equation_input = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" # (-0.4751, 0.9052)
            equation_input = "-4 * X^0 + 3 * X^0 + 4 * X^1 - 1.956425 * X^2 = 1 * X^0"
            equation_input = "5 * X^0 + * X^1 = 3 * X^0" # invalid coefficient
            equation_input = "5 * X^0 + 9 X^1 = 3 * X^0" # whitout star
            equation_input = "-X + 5.1 + 4 * X + X^2 = X^2 + 9" # freeform
        else:
            equation_input = input('Enter the polynomial equation:')

        validate_input(equation_input)
        computor(equation_input)

    except (KeyError, TypeError, ValueError, SyntaxError, IndexError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the application with optional debug mode.")
    parser.add_argument('--debug', action='store_true', help="Enable debug mode")
    args = parser.parse_args()
    
    main(debug=args.debug)