import random

def get_random_math_problem(max_value=100):
    """Returns a random math problem as a tuple (operation, operand1, operand2)."""
    operation = random.choice(['+', '-', '*', '/'])
    operand1 = random.randint(1, max_value)
    operand2 = random.randint(1, max_value)
    return (operation, operand1, operand2)
