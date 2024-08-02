print("Welcome to computor!")
print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
#equation_input = input('Enter the polynomial equation:')

print("--- ---- SOLUTION ---- ---")

def findpower(part, power):
    """Searches for the power parts and returns them"""
    num = part.split(f"*X^{power}")
    return num[0]

def parsel_the_equation(equation):
    """Parse the polynomial equation in the specified format and return the coefficients a, b, and c."""
    # Remove spaces
    equation = equation.replace(' ', '')
    
    # Split the equation into LHS and RHS
    lhs, rhs = equation.split('=')



    print("lhs: ", lhs)
    print("rhs", rhs)

    print("powers: ", findpower(lhs, 0))


parsel_the_equation("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
#parsel_the_equation(equation_input)
# print(equation_input)