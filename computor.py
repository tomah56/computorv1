import re
import math


def check_polynomial_degree(polynomial):
    """Checks if there are any higher than quadratic polynomial expression"""
    # Regular expression to find all exponents in the polynomial
    exponents = re.findall(r'X\^(\d+)', polynomial)
    
    # Convert exponents to integers
    exponents = [int(exp) for exp in exponents]
    
    # If there are no exponents found, return degree 0
    if not exponents:
        return 0
    
    # Find the maximum exponent, which is the degree of the polynomial
    max_degree = max(exponents)
    if max_degree > 2:
        print(f"I can't solve a {max_degree} Degree polynomial!")
        raise SystemExit("Stopping the code here.")


def findCoefficients(eq):
    """Gets the reduced form polinomial (max quadtratic) and return the coefficients a, b, and c."""
    print("powers: ")
    powers = 0
    coefficients = {0: 0, 1: 0, 2: 0}
    while powers < 3:
        pattern = rf'([-+]?\d*\.?\d+)\s*\*\s*X\^{powers}'
        numbers = [float(match.group(1)) for match in re.finditer(pattern, eq)]
        total_sum = sum(numbers)
        print(f"For the power of '{powers}' this numbers were found {numbers}. Sum: {total_sum}")
        coefficients[powers] = total_sum
        powers += 1
    return coefficients


def parsel_the_equation(equation):
    """Parse the polynomial equation in a combined format and returns it"""
    # Remove spaces
    equation = equation.replace(' ', '')

    # Split the equation into LHS and RHS
    lhs, rhs = equation.split('=')
    modified_rhs = ''
    for char in rhs:
        if char == '+':
            modified_rhs += '-'
        elif char == '-':
            modified_rhs += '+'
        else:
            modified_rhs += char

    if rhs[0] == '-':
        combined_equation = lhs + modified_rhs
    else:
        combined_equation = lhs + '-' + modified_rhs
    return combined_equation


def solve_eq(coefficients):
    """Solving the polynomial based on the quadtratic solution formula and returns the roots"""
    a = coefficients[2]
    b = coefficients[1]
    c = coefficients[0]
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        print("Two real and distinct roots:")
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        print("One real root:")
        root = -b / (2 * a)
        return root,
    else:
        print("No real roots, but two complex roots:")
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

