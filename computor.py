import re
import math


print("Welcome to computor!")
print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
#equation_input = input('Enter the polynomial equation:')

print("--- ---- SOLUTION ---- ---")

def get_polynomial_degree(polynomial):
    # Regular expression to find all exponents in the polynomial
    exponents = re.findall(r'X\^(\d+)', polynomial)
    
    # Convert exponents to integers
    exponents = [int(exp) for exp in exponents]
    
    # If there are no exponents found, return degree 0
    if not exponents:
        return 0
    
    # Find the maximum exponent, which is the degree of the polynomial
    max_degree = max(exponents)
    
    return max_degree

def findCoefficients(eq):
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
    """Parse the polynomial equation in the specified format and return the coefficients a, b, and c."""
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
  

#reducedform = parsel_the_equation(equation_input)
reducedform =  parsel_the_equation("-4 * X^0 + 3 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
degree = get_polynomial_degree(reducedform)

if degree > 2:
    print(f"I can't solve a {degree} Degree polynomial!")
    raise SystemExit("Stopping the code here.")

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
    # print(equation_input)