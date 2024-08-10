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



    print("lhs: ", lhs)
    print("rhs", rhs)

    print("powers: ")
    test = findpower(lhs, 0)
    # test.pop()
    print(len(test))
    while len(test):
        if test[0] - 5 > -1:
            if lhs[test[0] - 5] == '-':
                coefficients[0] -= int(lhs[test[0] - 4])
            elif lhs[test[0] - 5] == '+':
                coefficients[0] += int(lhs[test[0] - 4])
        elif test[0] - 5 == 0:
                coefficients[0] += int(lhs[test[0] - 4])
        test.pop(0)

    

    #print(lhs[test[0] - 4])
    print(coefficients)


parsel_the_equation("-4 * X^0 + 3 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
#parsel_the_equation(equation_input)
# print(equation_input)