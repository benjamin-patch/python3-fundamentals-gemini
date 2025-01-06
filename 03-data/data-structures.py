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

# 3. Sets
# Characteristics: Unordered, mutable, no duplicates, efficient for membership checks.
# Common Use Cases: Removing duplicates from a collection, performing set operations (union, intersection, etc.).

my_set = {1, 2, 2, 3}  # Duplicates are automatically removed

print(my_set)  # Output: {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# 4. Dictionaries
# Characteristics: Unordered, mutable, stores key-value pairs, keys must be unique and immutable.
# Common Use Cases: Representing structured data, efficient lookups by key, creating mappings.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

print(my_dict["name"])  # Accessing value by key (output: Alice)
my_dict["age"] = 31  # Modifying a value
my_dict["country"] = "USA"  # Adding a new key-value pair
print(my_dict)
