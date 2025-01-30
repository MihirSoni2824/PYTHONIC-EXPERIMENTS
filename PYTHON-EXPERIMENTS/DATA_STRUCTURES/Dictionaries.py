# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Modifying values
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding new key-value pairs
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}