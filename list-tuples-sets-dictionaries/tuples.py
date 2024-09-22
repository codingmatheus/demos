"""
Tuples are ordered collections of items that are immutable, meaning their contents cannot be changed once they are defined. Here are some key points about tuples:

1. Tuples are immutable: Once a tuple is created, its contents cannot be changed.
2. Tuples are defined using parentheses: They are defined using parentheses (), with items separated by commas.
3. Tuples can contain different data types: You can mix integers, strings, and other objects in a single tuple.
4. Tuples are zero-indexed: The first item in a tuple has an index of 0.
5. Tuples are immutable: Once a tuple is created, its contents cannot be changed.
6. Tuples can have performance advantages over lists: Due to their immutability, tuples can be more memory-efficient and faster in certain operations.

These advantages make tuples particularly useful for storing fixed collections of data where immutability is desired or where it could be safely applied for performance reasons.

"""

# Creating tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing tuple items
print(my_tuple[0])  # Output: 1
print(my_tuple[-1]) # Output: 5
