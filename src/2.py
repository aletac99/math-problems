import random

def get_random_math_problem():
    numbers = list(range(1, 10))
    operator = ["+", "-", "*", "/"]
    problem = f"{numbers[0]} {operator[random.randint(0, len(operator) - 1)]} {numbers[1]}"
    return eval(problem)