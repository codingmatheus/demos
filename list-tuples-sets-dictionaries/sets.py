"""
Sets are unordered collections of unique elements. Here are some key points about sets:

1. Sets are unordered: The elements in a set are not stored in any specific order.
2. Sets are mutable: You can add or remove elements after the set is created.
3. Sets are defined using curly braces: They are defined using curly braces {}, with elements separated by commas.
4. Sets are unordered: The elements in a set are not stored in any specific order.

"""

# Creating sets
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
