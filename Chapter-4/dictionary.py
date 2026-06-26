marks = {
    "A": 90,
    "B": 80,
    "C": 70,
    "list": [1, 2, 3],
}

print(marks)  # Output: {'A': 90, 'B': 80, 'C': 70, 'list': [1, 2, 3]}
print(type(marks))  # Output: <class 'dict'>
print(marks["A"])  # Output: 90
print(marks["B"])  # Output: 80
print(marks["C"])  # Output: 70
print(marks["list"])  # Output: [1, 2, 3]
#It is mutable, so we can change the value of a key
marks["A"] = 95
print(marks)  # Output: {'A': 95, 'B': 80, 'C': 70, 'list': [1, 2, 3]}

# Built-in functions
print(marks.keys())  # Output: dict_keys(['A', 'B', 'C', 'list'])
print(marks.values())  # Output: dict_values([95, 80, 70, [1, 2, 3]])
print(marks.items())  # Output: dict_items([('A', 95), ('B', 80), ('C', 70), ('list', [1, 2, 3])])
marks.update({"C": 75})  # Update the value of key "C"
print(marks)  # Output: {'A': 95, 'B': 80, 'C': 75, 'list': [1, 2, 3]}
