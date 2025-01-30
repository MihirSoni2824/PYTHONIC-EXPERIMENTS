# Creating a list
my_list = [1, 2, 3, "hello", True]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True

# Slicing
print(my_list[1:3])  # Output: [2, 3]

# Modifying elements
my_list[2] = 4
print(my_list)  # Output: [1, 2, 4, "hello", True]

# Adding elements
my_list.append("world")
print(my_list)  # Output: [1, 2, 4, "hello", True, "world"]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [1, 4, "hello", True, "world"]