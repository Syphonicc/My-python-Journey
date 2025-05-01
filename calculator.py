#Python Calculator
add = "+"
sub = "-"
mul = "*"
div = "/"

operator = input("Enter an operator ( + - * /):")
num1 = float(input("Enter the 1st number:"))
num2= float(input("Enter the 2nd number:"))

if operator == add:
    result = num1 + num2
    print(result)
elif operator == sub:
    result = num1 - num2
    print(result)
elif operator == mul:
    result = num1 * num2
    print(result)
elif operator == div:
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not valid")


