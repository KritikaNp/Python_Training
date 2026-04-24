# Print numbers 1 to 10 using while loop
num=1
while num!=11:
    print(num)
    num+=1

# Ask user to enter numbers until they enter 0, then print the sum of all entered numbers
number=" "
while number!=0:
    number=int(input("Enter a number: "))
    if number!=0:
        print("Try again")
    else:
        print("Great job")

# Write a number guessing game — computer picks a number between 1-10, user keeps guessing until correct
import random
secret = random.randint(1, 10)  # this picks random number
guess=int(input("Enter you guess(1-10): "))
while guess!=secret:
    print("Try again!")
    guess=int(input("Enter you guess: "))
print("Yay!! you guessed the number")

'''Ask user to enter a password, keep asking until they enter a password that:

Is more than 8 characters
Contains a number'''
password=""
while True:
    password=input("Enter a password (minimum 9 characters, Contains a number):")
    if any(char.isdigit() for char in password) and len(password) > 8:
        print("Password approved")
        break
    else:
        print("Try again! Password doesn't meet the requirement")

# Print this pattern using while loop:
# *
# **
# ***
# ****
# *****
i = 1
while i <= 5:
    j = 0
    while j < i:
        print('*',end="")
        j+=1
    print()
    i+=1

# ATM system
correct_pin = "1234"
attempts = 0

while attempts != 3:
    pin = input("Enter PIN: ")
    attempts += 1
    if pin == correct_pin:
        print(f"Access granted! Took {attempts} attempts")
        break
    else:
        print("Wrong PIN!")
else:                           
    print("Card blocked!")  
