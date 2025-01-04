name = "Alice"
age = 30
print("My name is", name, "and I am", age, "years old.")

# **Separating Multiple Items**

# In Python, the `print()` function can take multiple arguments separated by commas. These arguments can be:

# * **Strings:** Like "My name is" or "years old."
# * **Variables:** Like `name` and `age`.
# * **Numbers:**  Like the number 5 or 3.14.

# The commas act as separators, telling Python to treat each item as a distinct element to be included in the output.

# **How it Works**

# When you run `print("My name is", name, "and I am", age, "years old.")`, Python does the following:

# 1. **Evaluates Variables:**  It replaces the variables `name` and `age` with their respective values ("Alice" and 30).
# 2. **Concatenates with Spaces:** It joins all the items together, inserting a space between each one.
# 3. **Prints the Result:** It displays the combined string "My name is Alice and I am 30 years old." on the console.

# **Example without Commas**

# If you were to remove the commas and write:

# ```python
# print("My name is"name"and I am"age"years old.") 
# ```

# Python would treat the entire sequence of characters as a single string literal, resulting in the output:

# ```
# My name isAliceand I am30years old.
# ```

# This clearly shows how important those commas are for readability!

# **Key Takeaway**

# Commas in `print()` help you combine different types of data (strings, variables, numbers) into a formatted output, making your printed information clear and organized.
