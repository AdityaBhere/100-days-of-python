from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

functions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)
    use_over = False

    num_1 = float(input("What is the first number?: "))

    while not use_over:
        for ops in functions:
            print(ops)

        operation = input("Pick an operation: ")
        num_2 = float(input("What is the next number?: "))

        result = functions[operation](num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}, "
            f"or type 'n' to start a new calculation: "
        )

        if choice == 'y':
            num_1 = result
        else:
            use_over = True
            print("\n" * 20)
            calculator()

calculator()
