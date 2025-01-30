class NegativeNumberError(Exception):
    pass

def calculate_square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return num ** 0.5

try:
    result = calculate_square_root(-4)
except NegativeNumberError as e:
    print(e)