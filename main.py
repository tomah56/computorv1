import argparse
from computor import *

def main(debug):
    try:
        print("Welcome to computor!")
        print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
        if debug:
           equation_input = "-4 * X^0 + 3 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
        else:
           equation_input = input('Enter the polynomial equation:')
       
        reducedform = parsel_the_equation(equation_input)
        check_polynomial_degree(reducedform)
        coefficients = findCoefficients(reducedform)

        print("Reduced form:")
        print(f"{coefficients[2]} * X^2 + ({coefficients[1]}) * X^1 + ({coefficients[0]}) * X^0 = 0")

        print("Coefficients:", coefficients)

        if all(coef == 0 for coef in coefficients):
            print("The equation is an identity. Every x is a solution")
        elif coefficients[0] != 0 and coefficients[1] == 0 and coefficients[2] == 0:
            print("The equation is an Contradiction. There is no solution")
        else:
            if coefficients[2] != 0:
                print("Degree 2 - quadratic")
            elif coefficients[1] != 0:
                print("Degree 1 - linear")
            elif coefficients[0] != 0:
                print("Degree 0 - non-zero constant")

            roots = solve_eq(coefficients)

            print(roots)
    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()