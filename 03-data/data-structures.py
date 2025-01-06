# Python Data Structures

# 1. Lists
# Characteristics: Ordered, mutable (changeable), allows duplicates, versatile.
# Common Use Cases: Storing collections of items, managing sequences, general-purpose data storage.

my_list = [1, 2.5, "hello", True]  # A list with mixed data types

print(my_list[0])  # Accessing the first element (output: 1)
my_list.append(5)  # Adding an element to the end
my_list.insert(2, "world")  # Inserting at a specific index
print(my_list)  # Output: [1, 2.5, 'world', 'hello', True, 5]

# 2. Tuples
# Characteristics: Ordered, immutable (unchangeable after creation), allows duplicates.
# Common Use Cases: Representing fixed collections, ensuring data integrity, situations where data shouldn't be modified.

my_tuple = (10, 20, "python")

print(my_tuple[1])  # Accessing the second element (output: 20)
# my_tuple[1] = 30  # This would raise an error because tuples are immutable
