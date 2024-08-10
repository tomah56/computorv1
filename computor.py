import re

print("Welcome to computor!")
print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
#equation_input = input('Enter the polynomial equation:')

print("--- ---- SOLUTION ---- ---")

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

    print("Reduced form: ")
    print(combined_equation, "= 0")
    return combined_equation

  

    #print(lhs[test[0] - 4])


#reducedform = parsel_the_equation(equation_input)
reducedform =  parsel_the_equation("-4 * X^0 + 3 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
coefficients = findCoefficients(reducedform)
print("Coefficients:", coefficients)
# print(equation_input)