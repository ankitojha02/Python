# 1 for snake, -1 for water, 0 for gun
computer_choice = 0
you_choice = int(input("Enter your choice (1 for snake, -1 for water, 0 for gun): "))

if you_choice == computer_choice:
    print("It's a tie!")
elif (you_choice == 1 and computer_choice == -1) or (you_choice == -1 and computer_choice == 0) or (you_choice == 0 and computer_choice == 1):
    print("You win!")
else:
    print("Computer wins!")
