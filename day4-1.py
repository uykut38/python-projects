def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))


if operator == "+":
    result = add(num1, num2)

elif operator == "-":
    result = sub(num1, num2)

elif operator == "*":
    result = mul(num1, num2)

elif operator == "/":
    result = div(num1, num2)

else:
    result = "Invalid operator"


print("Result is:", result)