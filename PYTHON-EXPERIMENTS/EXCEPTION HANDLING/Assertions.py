def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

result = divide(10, 2)
print(result)  # Output: 5

# Trying to divide by zero will raise an AssertionError
result = divide(10, 0)