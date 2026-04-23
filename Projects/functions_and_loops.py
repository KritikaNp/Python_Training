# Write a function that takes a list of numbers and returns the largest number without using max()
def largest_number(x):
    maximum=x[0]
    for number in x:
        if number > maximum:
            maximum=number
    return maximum

numbers=[2,5,3,86,9,334,65]
maximum=largest_number(numbers)
print(maximum)


#  Write a function that takes a name and prints it 5 times
def repeat_name(name):
    for i in range(5):
        print(name)

repeat_name("Aarav")


# Write a function that takes a list and returns only the even numbers from it
def even_numbers(a):
    even_list=[]
    for number in a:
        if number % 2 == 0:
            even_list.append(number)
    return even_list
print(even_numbers(numbers))


# Write a function that checks if a number is prime or not
def is_prime(number):
    for i in range(2,(number-1)):
        if number % i==0:
            print(f"{number} is composite")
            return
    print(f"{number} is prime")

is_prime(7)  # True
is_prime(10)  # False


# Write a function that takes a list of names and returns the longest name
def longest_name(names):
    long=names[0]
    for name in names:
        if len(name) > len(long):
            long=name
    return long

names=["Sadikshya","Swastika","Parista","Sabnam","Sushma"]
longestname=longest_name(names)
print(longestname)