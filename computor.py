import re
import math


def is_number(term):
    """Check if a term is a number (integer or floating-point)."""
    try:
        float(term)  # Try converting the term to a float
        return True
    except ValueError:
        return False

def is_number_times_x(term):
    """Check if the term is in the format 'number*X'."""
    pattern = re.compile(r'^\d+(\.\d+)?\*X$')
    return bool(pattern.match(term))

def is_missing_num(term):
    """Check if the term is in the format 'X^2' missing a the number."""
    pattern = re.compile(r'^X\^2$')
    return bool(pattern.match(term))

def replace_power(term):
    return f"{term}*X^0"

def replace_single_x(term):
    return f"{term}^1"

def replace_number(term):
    return f"1*{term}"

def validate_input(equation):
    # Ensure the input is a string
    if not isinstance(equation, str):
        raise TypeError("Input must be a string.")
    
    # Check for valid characters
    allowed_characters = re.compile(r'^[0-9\.\+\-\*\^X\s=]+$')
    if not allowed_characters.match(equation):
        raise ValueError("Input contains invalid characters.")

    # Check that the equation has exactly one '=' sign
    sides = equation.split('=')
    if len(sides) != 2:
        raise SyntaxError("Equation must have exactly one '=' sign.")
    return "Input is valid"

def level_II_validator(equation):
      # Check for valid term syntax
    term_pattern = re.compile(r'^\s*-?\d+(\.\d+)?\s*\*\s*X\^\d+\s*$')
    pattern = re.compile(r'\d*\.\d+|\d+ \* X|\d+X|\d+\*X|X\^2|X|\d+|[+\-*/^]')
    terms = pattern.findall(equation)
    # print("--   --- ----    OLD :", terms)
    new_terms = []
    for term in terms:
        term = term.strip()
        if term and not term_pattern.match(term):
            # if  is_valid_string(term):
            if is_number(term):
                new_terms.append(replace_power(term))
            elif is_number_times_x(term):
                new_terms.append(replace_single_x(term))
            elif is_missing_num(term):
                new_terms.append(replace_number(term))
            elif term == 'X':
                new_terms.append(replace_number(replace_single_x(term)))
            elif term == '^':
                raise SyntaxError("Equation muissing power")
            else:
                new_terms.append(term)
    # print("--   --- ----    NEW :", new_terms)
    return ''.join(new_terms)
 
def level_III_validator(equation):
      # Check for valid term syntax
    pattern = r'^([-+]?\s*\d*\.?\d*)\s*\*\s*X\^(\d+)\s*([+-]\s*\d*\.?\d*\s*\*\s*X\^\d+)*$'

    # Match the cleaned expression against the pattern
    match = re.fullmatch(pattern, equation)
    
    # Additional checks to ensure proper term formats
    if match:
        # Check if every term follows the pattern correctly
        terms = re.findall(r'([-+]?\s*\d*\.?\d*)\s*\*\s*X\^(\d+)', equation)
        for term in terms:
            coefficient, power = term
            if not coefficient and power:  # Missing coefficient case
                raise SyntaxError("Wrong syntax")
    else:
        raise SyntaxError("Wrong syntax")
 


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
        raise ValueError("The program only handles quadratic equations.")


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
    print("Discriminant: ", discriminant)
    # Check if the discriminant is positive, zero, or negative
    if a != 0:
        print("Formula:")
        print(f"\n        {-b} + √({b}^2 - 4 * {a} * {c})\n      -------------------------------------\n                   (2 * {a})\n")
        if discriminant > 0:
            print("Two real and distinct roots:")
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2
        elif discriminant == 0:
            print("One real root:")
            root = -b / (2 * a)
            # BUG it should check if its float before
            print("Fraction:")
            print(f"\n      {-1 * int(b)}\n    -----\n      {int(2 * a)}\n")
            return root,
        else:
            print("No real roots, but two complex roots:")
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            return root1, root2
    elif b != 0:
        # BUG it should check if its float before
        print("Fraction:")
        print(f"\n      {-1 * int(c)}\n    -----\n      {int(b)}\n")
        return -c / b

def computor(poli):
    reducedform = parsel_the_equation(poli)
    print(f"Reordered form: {reducedform} = 0")
    check_polynomial_degree(reducedform)
    new_string = level_II_validator(reducedform)
    # print(new_string)
    level_III_validator(new_string)
    coefficients = findCoefficients(new_string)

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
        return roots