try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("An unexpected error occurred:", e)