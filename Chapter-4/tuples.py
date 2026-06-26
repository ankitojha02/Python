# tuples are immutable sequences, typically used to store collections of heterogeneous data. Tuples are defined by enclosing the elements in parentheses ().
a = (1, 2, 3)
b = (4, 5, 6)
print(type(a))  # Output: <class 'tuple'>

#Built-in functions
a.count(2)  # Count the number of occurrences of 2 in the tuple
print(a.count(2))  # Output: 1
a.index(3)  # Find the index of the first occurrence of 3 in the tuple
print(a.index(3))  # Output: 2
