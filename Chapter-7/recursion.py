# Recursive function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# when to use recursion - when a problem can be broken down into smaller, similar subproblems
