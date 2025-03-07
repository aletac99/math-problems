def solve_math_problem():
    # Generate a random math problem
    operand1 = random.randint(0, 10)
    operator = random.choice(["+", "-", "*", "/"])
    operand2 = random.randint(0, 10)
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    else:
        result = operand1 / operand2

    # Return the solution
    return result
