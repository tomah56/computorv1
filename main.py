import argparse
from computor import computor

def main(debug):
    try:
        print("Welcome to computor!")
        print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
        if debug:
            print("Debug mode! no user imput.")
            equation_input = "-4 * X^0 + 3 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
            equation_input = "1 * X^0 + 2 * X^1 - 1 * X^2 = 0"
            equation_input = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" # (-0.4751, 0.9052)
            equation_input = "5 * X^0 + 4 * X^1 = 4 * X^0"
            equation_input = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
        else:
            equation_input = input('Enter the polynomial equation:')
       
        computor(equation_input)

    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the application with optional debug mode.")
    parser.add_argument('--debug', action='store_true', help="Enable debug mode")
    args = parser.parse_args()
    
    main(debug=args.debug)