"""
Dictionaries are unordered collections of key-value pairs. Here are some key points about dictionaries:

1. Dictionaries are mutable: You can add, remove, or modify key-value pairs after the dictionary is created.
2. Dictionaries are defined using curly braces: They are defined using curly braces {}, with key-value pairs separated by commas.
3. Key-value pairs are defined using a colon ":": The key and value are separated by a colon.
4. Dictionaries are unordered: The items in a dictionary are not stored in any specific order.
"""

# Creating dictionaries
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

# Getting all keys and values
print(my_dict.keys())  # Output: dict_keys(['apple', 'cherry', 'date'])
print(my_dict.values())  # Output: dict_values([1, 3, 4])

# Accessing dictionary items
print(my_dict['apple'])  # Output: 1

# Checking if a key exists
if 'apple' in my_dict:
    print("Apple is in the dictionary")

# If you try to access a key that doesn't exist, you'll get a KeyError. You can avoid this by using the get method.
print(my_dict.get('grape'))  # Output: None

# You can also use the get method to provide a default value if the key doesn't exist.
print(my_dict.get('grape', 'Not found'))  # Output: 'Not found'

# Adding new key-value pairs
my_dict['date'] = 4
print(my_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

# Removing key-value pairs
del my_dict['banana']
print(my_dict)  # Output: {'apple': 1, 'cherry': 3, 'date': 4}









