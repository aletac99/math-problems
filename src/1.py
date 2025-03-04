import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Get a random operator (+, -, *, /)
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    
    # Create the math problem
    problem = f"{num1} {operator} {num2} = "
    
    # Get the solution
    solution = eval(problem)
    
    return problem, solution
