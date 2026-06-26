s = {1, 2, 3}
# Sets are unordered collections of unique elements. They are defined by enclosing the elements in curly braces {}.
# No duplicates are allowed in a set, and the order of elements is not guaranteed.

# Empty set
empty_set = set()  # Use set() to create an empty set
print(type(s))  # Output: <class 'set'>
print(type(empty_set))  # Output: <class 'set'>

s1 = {1, 5, 23, 455, "Ankit"}
s1.add(100)  # Add an element to the set
print(s1)  # Output: {1, 5, 23, 455, "Ankit", 100}

# Built-in functions
print(len(s1))  # Output: 6
print(1 in s1)  # Output: True
s1.remove(5)  # Remove an element from the set
