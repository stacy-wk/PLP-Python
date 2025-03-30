#Enter and save input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
mathOperation = input("Enter an operation (+, -, *, /): ")

#Calculation depending on the math operation
if mathOperation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif mathOperation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif mathOperation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif mathOperation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("MATH ERROR! Division by zero is not allowed.")
else:
    print("Invalid operation.")