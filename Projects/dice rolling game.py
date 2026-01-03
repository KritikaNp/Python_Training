import random
count=0
no_of_dice=input("How many dice do you want to roll? (1 or 2): ")
if no_of_dice=="1":
    while True:
        choice=input("Roll the dice? (y/n):").lower()

        if choice== 'y':
            dice1 = random.randint(1,6)
            print(f"({dice1})")
            count+=1
        elif choice== 'n':
            print("Thanks for playing!")
            break  
        else:
            print("Invalid choice!")
elif no_of_dice=="2":
    while True:
        choice=input("Roll the dice? (y/n):").lower()

        if choice== 'y':
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print(f"({dice1},{dice2})")
            count+=1
        elif choice== 'n':
            print("Thanks for playing!")
            break  
        else:
            print("Invalid choice!")
else:
      print("Please only enter 1 or 2")  

print(f"Number of times the dice have been rolled:{count}")
