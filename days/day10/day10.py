from calc_logo import calc_logo

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(calc_logo)
    calculating = True
    first_number = float(input("What's the first number?: "))
    while calculating:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick the operation symbol")
        second_number = float(input("What's the next number?: "))
        result = 0


        if operation_symbol in operations:
            result = operations[operation_symbol](first_number, second_number)
            print(f'{first_number} {operation_symbol} {second_number} = {result}')


        choice_to_continue = input(
            f'Type {"y"} to continue calculating with {result}, or type {'n'} to start a new calculation: ')
        if choice_to_continue == 'y':
            first_number = result
        else:
            calculating = False
            print("\n" * 20)
            calculator()


calculator()

