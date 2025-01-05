# Operators: Symbols that perform operations on data (like +, -, *, /, ==, <, >).

sum = 5 + 3
product = 5 * 3
is_equal = 5 == 5

# `=` (Assignment Operator)
# Purpose: This operator is used to assign a value to a variable.

x = 5  # Assigns the value 5 to the variable x
name = "Bob"  # Assigns the string "Bob" to the variable name

# Direction: Think of it as a one-way operation.
# The value on the right side is assigned to the variable on the left side.

# `==` (Equality Comparison Operator)
# Purpose: This operator compares two values to see if they are equal.

x == 5  # Checks if the value of x is equal to 5
name == "Alice" # Checks if the value of name is equal to "Alice"

# Result: It returns `True` if the values are equal and `False` if they are not.
# Direction: This is a two-way comparison – the order of the values doesn't matter (5 == x is the same as x == 5).

# Analogy
# Imagine a box labeled "x".
x = 5 # is like putting the number 5 into the box.
x == 5 # is like looking into the box and asking, "Is the number 5 in this box?"

# Common Mistake
# It's very common for beginners (and even experienced programmers sometimes!) to accidentally use `=` when they mean `==`, especially in conditional statements.
# This can lead to unexpected behavior in your code.

# Example
x = 5 
if x = 5:  # This is incorrect! It should be x == 5
    print("x is 5")

# In this incorrect code, the `if` statement would always evaluate to `True` because the assignment `x = 5` itself returns a value (which is considered "truthy" in Python).
