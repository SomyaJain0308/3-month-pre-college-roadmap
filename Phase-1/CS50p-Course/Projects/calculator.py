def add(num_1, num_2):
    Z = num_1 + num_2
    print(f"{num_1} + {num_2} = {Z}")
def subtract(num_1, num_2):
    Z = num_1 - num_2
    print(f"{num_1} - {num_2} = {Z}")
def multiply(num_1, num_2):
    Z = num_1 * num_2
    print(f"{num_1} * {num_2} = {Z}")
def divide(num_1, num_2):
    if num_2 != 0:
        Z = num_1 / num_2
        print(f"{num_1} / {num_2} = {Z}")
    else:
        print("0 cannot be a divisor dumbass!")
def modulo(num_1, num_2):
    if num_2 != 0:
        Z = num_1 % num_2
        print(f"{num_1} % {num_2} = {Z}")
    else:
        print("Cannot calculate remainder when dividing by zero!")
print("--------------------------------------------------------------------------------------")
print("Hi Nerd!")
print("Let's do Math!")
print("FORMAT:")
print("X _ Y")
print("--------------------------------------------------------------------------------------")
try:
    num_1 = float(input("What's X? "))
    num_2 = float(input("What's Y? "))
    op = input("What's the operator? (Choose from [+, -, *, /, %]) ")
    print("--------------------------------------------------------------------------------------")

    if op == "+":
        add(num_1, num_2)
    elif op == "-":
        subtract(num_1, num_2)
    elif op == "*":
        multiply(num_1, num_2)
    elif op == "/":
        divide(num_1, num_2)
    elif op == "%":
        modulo(num_1, num_2)
    else:
        print("Invalid Operator!")
except ValueError:
    print("Invalid Number!")
