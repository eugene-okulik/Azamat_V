def decorator(func):
    def wrapper(a, b, operation=None):
        if a == b:
            operation = "+"
        elif a > b:
            operation = "-"
        elif b > a > 0:
            operation = "/"
        if a < 0 or b < 0:
            operation = "*"

        return func(a, b, operation)

    return wrapper


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))


@decorator
def calc(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return second_number - first_number
    elif operation == "/":
        return first_number / second_number
    elif operation == "*":
        return first_number * second_number


result = calc(first, second)
print(f"Result: {result}")
