print("Welcome to computor!")
print("Usage. (e.g. a * X^0 + b * X^1 - c * X^2 = d * X^0)")
#equation_input = input('Enter the polynomial equation:')

print("--- ---- SOLUTION ---- ---")

def findpower(eq, power):
    """Searches for the coefficients and returns the positions"""
    power_str = str(power)
    positions = []
    start = 0
    while True:
        # get the position of the coefficient starting from the 'start' index
        position = eq.find(power_str, start)
        
        # If the substring is found, add the position to the list and update 'start'
        if position != -1:
            positions.append(position)
            start = position + 1
        else:
            break

    # Print the result
    if positions:
        print(f"The coefficient '{power_str}' was found at positions: {positions}.")
    else:
        print(f"The coefficient '{power_str}' was not found.")

    return positions

def parsel_the_equation(equation):
    """Parse the polynomial equation in the specified format and return the coefficients a, b, and c."""
    # Remove spaces
    equation = equation.replace(' ', '')
    coefficients = {0: 0, 1: 0, 2: 0}

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
    


    #print("lhs: ", lhs)
#    print("rhs", rhs)

    print("Reduced for: ")
    print(combined_equation, "= 0")
    print("powers: ")
    powers = 0
    while powers < 3:
        test = findpower(combined_equation, powers)
        while len(test):
            if test[0] - 5 > -1:
                if combined_equation[test[0] - 5] == '-':
                    coefficients[powers] -= int(combined_equation[test[0] - 4])
                elif combined_equation[test[0] - 5] == '+':
                    coefficients[powers] += int(combined_equation[test[0] - 4])
            elif test[0] - 5 == 0:
                    coefficients[powers] += int(combined_equation[test[0] - 4])
            test.pop(0)
        powers += 1

    

    #print(lhs[test[0] - 4])
    print(coefficients)


parsel_the_equation("-4 * X^0 + 3 * X^0 + 4 * X^1 - 3 * X^2 = 1 * X^0")
#parsel_the_equation(equation_input)
# print(equation_input)