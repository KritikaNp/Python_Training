#  Print numbers 1 to 10 using a for loop
for i in range(1,11):
    print(i)


# Print all even numbers from 1 to 20
for j in range(2,21,2):
    print(j)


# Make a list of 5 of your favorite foods and print each one
foods=["Mo:Mo","Keema Noodles","Paneer","Thukpa","Current Noodles"]
print("My favourite foods are: ")
for food in foods:
    print(food)


# From this list find and print only numbers greater than 10
numbers = [3, 15, 7, 22, 8, 19, 4, 11]

for num in numbers:
    if num > 10:
        print(num)


# Count how many numbers are greater than 10 in that same list
count = 0
print("numbers greater than 10 in the list: ")
for num in numbers:
    if num > 10:
        count=count+1

print(count)


#  Make a list of 5 names and print only names that have more than 5 letters
names=["Kritika","Swastika","Susma","Parista","Suman"]
for name in names:
    if len(name) > 5:
        print(name)


# Print multiplication table of any number the user inputs
num=int(input("Enter a number you want multiplication table of: "))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")


# From a list of numbers print whether each number is odd or even
list_of_numbers=[5,64,13,34,19,66,32,12,9,3]
for number in list_of_numbers:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


# Make a list of 5 numbers and print their sum without using sum()
sum = 0
for number in list_of_numbers:
    sum=number+sum
print(f"Sum = {sum}")


# From this list remove all duplicates and print unique values only
digits = [1, 2, 2, 3, 4, 4, 5, 1]
unique_digits=[]
for dig in digits:
    if dig not in unique_digits:
        unique_digits.append(dig)
print(unique_digits)