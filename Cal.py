import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def sin(x):
    return math.sin(x)


def tan(x):
    return math.tan(x)


def cos(x):
    return math.cos(x)


def acos(x):
    return math.acos(x)


def asin(x):
    return math.asin(x)


def atan(x):
    return math.atan(x)


def log(x):
    return math.log(x)


def sqrt(x):
    return math.sqrt(x)


def average(numbers):
    return sum(numbers) / len(numbers)


def percentage(part, whole):
    return (part / whole) * 100


def power(x, y):
    return x ** y


def cube(x):
    return x ** 3


#  Some function called

result = add(10, 15)
print(result)  # prints 15

result = subtract(10, 15)
print(result)  # prints 5

result = multiply(10, 15)
print(result)  # prints 50

result = divide(15, 10)
print(result)  # prints 2

result = sin(math.pi / 3)
print(result)  # prints 1.0

result = average([1, 2, 3])
print(result)  # prints 2.0

result = percentage(10, 100)
print(result)  # prints 5.0
