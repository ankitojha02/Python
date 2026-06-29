a = int(input("Enter a number: "))

for i in range(1, 11):
    result = a * i
    print(f"{a} x {i} = {result}")

l = ["apple", "banana", "cherry"]
for x in l:
    if(x.startswith("b")):
        print(x)
