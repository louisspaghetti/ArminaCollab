import random

running = True
level = 0
moves_remaining = 0
starting_value = 1
operator = 2
operation_list = ["addition", "subtraction", "multiplication", "division"]

#recursive function that applies random operations to a base number to scramble it
def apply_operations(base, operator = 2, iterations = 1, index = random.randint(0,3)):
    operation = operation_list[index]
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


while running:
    if moves_remaining <= 0:
        level += 1
        current_value = apply_operations(starting_value, operator, level, random.randint(0,3))
        moves_remaining = level
    print(level)
    print(moves_remaining)
    print(current_value)
    print("Enter the operation")
    current_value = apply_operations(current_value, operator, 1, operation_list.index(input()))
    moves_remaining -= 1