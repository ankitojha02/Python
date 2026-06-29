# def average(a, b, c):
#     return (a + b + c) / 3

# x = 10
# y = 20
# z = 30

# print(f"The average of {x}, {y}, and {z} is: {average(x, y, z)}")

# def greet(name):
#     return f"Hello, {name}"

# name = input("Enter your name: ")
# print(greet(name))

#default argument
def greet(name="Guest"):
    return f"Hello, {name}"

print(greet())  # Uses default argument
print(greet("Alice"))  # Uses provided argument
