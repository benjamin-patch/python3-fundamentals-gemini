# Python Data Structures

# 1. Lists
# Characteristics: Ordered, mutable (changeable), allows duplicates, versatile.
# Common Use Cases: Storing collections of items, managing sequences, general-purpose data storage.

my_list = [1, 2.5, "hello", True]  # A list with mixed data types

print(my_list[0])  # Accessing the first element (output: 1)
my_list.append(5)  # Adding an element to the end
my_list.insert(2, "world")  # Inserting at a specific index
print(my_list)  # Output: [1, 2.5, 'world', 'hello', True, 5]
