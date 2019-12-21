import random

running = True
level = 1
operation_list = ["addition", "subtraction", "multiplication", "division"]

#recursive function that applies random operations to a base number to scramble it
def apply_operations(base, operator = 2, iterations = 1):
    operation = operation_list[random.randint(0,3)]
    if iterations == 0:
        return base
    if operation == "addition":
        return apply_operations(base + operator, operator, iterations - 1)
    elif operation == "subtraction":
        return apply_operations(base - operator, operator, iterations - 1)
    elif operation == "multiplication":
        return apply_operations(base * operator, operator, iterations - 1)
    elif operation == "division":
        return apply_operations(base / operator, operator, iterations - 1)
    return

