try:
    # Code that might raise an exception
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
     if file:
        file.close()