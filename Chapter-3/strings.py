a = "Hello, World!"
print(a)  # Output: Hello, World!

b = a.upper()
print(b)  # Output: HELLO, WORLD!

c = a[3:8] #slice the string from index 3 to 7 (8 is not included)
print(c)  # Output: lo, W

d = len(a)
print(d)  # Output: 13

e = a[-1]  # Access the last character of the string
print(e)  # Output: !

print(a[:4]) # Output: Hell (slice from start to index 3)

#skipping characters in a string
f = a[1:7:2]
print(f)  # Output: el, (slice from index 1 to 6, skipping every 2nd character)

#built-in string methods
g = a.replace("World", "Python")
print(g)  # Output: Hello, Python!
print(a.endswith("!"))  # Output: True

print(a.startswith("Hello"))  # Output: True

name = "Alice"
print(f"Hello, {name}!")  # Output: Hello, Alice! (using f-string for string formatting
