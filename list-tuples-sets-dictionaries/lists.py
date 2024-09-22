"""
Python lists are versatile and commonly used data structures that allow you to store multiple items in a single variable. Here are some key points about lists:

1. Lists are ordered: Items in a list maintain their order.
2. Lists are mutable: You can change, add, or remove items after the list is created.
3. Lists can contain different data types: You can mix integers, strings, and other objects in a single list.
4. Lists use square brackets: They are defined using square brackets [], with items separated by commas.
5. Lists are zero-indexed: The first item in a list has an index of 0.

Lists support various operations and methods, such as appending, removing, and accessing items, as demonstrated in the examples below.

"""

# Accessing list items
fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[0])       # Output: 'apple' (first item)
print(fruits[-1])      # Output: 'date' (last item)
print(fruits[1:3])     # Output: ['banana', 'cherry'] (slicing)

# Changing list items
numbers = [1, 2, 3, 4, 5]
numbers[2] = 10        # Change the third item
print(numbers)         # Output: [1, 2, 10, 4, 5]

# Appending items to a list
colors = ['red', 'green', 'blue']
colors.append('yellow')    # Add 'yellow' to the end
print(colors)          # Output: ['red', 'green', 'blue', 'yellow']

colors.insert(1, 'orange') # Insert 'orange' at index 1
print(colors)          # Output: ['red', 'orange', 'green', 'blue', 'yellow']

# Extending a list
more_colors = ['purple', 'pink']
colors.extend(more_colors) # Add all items from more_colors to colors
print(colors)          # Output: ['red', 'orange', 'green', 'blue', 'yellow', 'purple', 'pink']

# Removing items from a list
animals = ['cat', 'dog', 'elephant', 'fish']
removed_animal = animals.pop()  # Remove and return the last item
print(removed_animal)  # Output: 'fish'
print(animals)         # Output: ['cat', 'dog', 'elephant']

animals.remove('dog')  # Remove the first occurrence of 'dog'
print(animals)         # Output: ['cat', 'elephant']

del animals[0]         # Remove item at index 0
print(animals)         # Output: ['elephant']

# Clearing a list
animals.clear()        # Remove all items from the list
print(animals)         # Output: []





