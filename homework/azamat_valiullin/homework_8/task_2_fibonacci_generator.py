import sys
sys.set_int_max_str_digits(50000)


def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def count(generator, a, b, c, d):
    for i, element in enumerate(generator):
        if i == a:
            print(f"fifth number: {element}")
        elif i == b:
            print(f"two hundredth number: {element}")
        elif i == c:
            print(f"thousandth number: {element}")
        elif i == d:
            print(f"one hundred thousandth number: {element}")
            break


count(fibonacci_sequence(), a=4, b=199, c=999, d=99999)
