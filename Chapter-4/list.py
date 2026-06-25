friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
Alice = [23, "Engineer", "New York"]
print(friends[0])  # Output: Alice
print(Alice[0])   # Output: 23
Alice[0] = 24  # Update Alice's age
print(Alice[0])   # Output: 24

for friend in friends:
    print(friend)

Roll = [101, 108, 103, 104, 105, 108, 110, 140, 128]
Roll.sort()  # Sort the list in ascending order
print(Roll)  # Output: [101, 103, 104, 105, 108, 108, 110, 128, 140]

# Built-in functions
print(len(friends))  # Output: 5
friends.append("Frank")  # Add a new friend to the list
print(friends)  # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
friends.remove("Charlie")  # Remove a friend from the list
print(friends)  # Output: ['Alice', 'Bob', 'David', 'Eve', 'Frank']
friends.pop()  # Remove the last friend from the list
print(friends)  # Output: ['Alice', 'Bob', 'David', 'Eve']
