import os
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operation_dictonary={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

def calculator():
    number1=float(int(input("Enter the first number:")))
    for symbol in operation_dictonary:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operation:")
        number2=float(int(input("Enter the next number:")))
        calculator_function=operation_dictonary[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2}={output}")

        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit:").lower()
        if should_continue=='y':
            number1=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()

        else:
            continue_flag=False
            print("Bye!")
calculator()








































