# index error
numbers=[1,2,3]
try:
    print(numbers[5])
except IndexError:
    print("The index doesn't exist")

# Handle this — user enters a number, catch if they enter text
try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except ValueError:
    print("That is not a number!")


# Handle division by zero
numerator=int(input("Enter a numerator:"))
denomiator=int(input("Enter a denominator:"))
try:
    result=numerator/denomiator
except ZeroDivisionError:
    print("The denominator cannot be zero")
else:
    print(f"Division={result}")

# Handle multiple errors at once
numbers = [1, 2, 3, 4, 5]
try:
    index=int(input("Enter index: "))
    print(numbers[index])
except ValueError:
    print("Enter a number for index not text")
except IndexError:
    print("The index doesn't exist")


# Use finally to print "Program finished" no matter what happens
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("The denominator cannot be 0")
except ValueError:
    print("Enter a number not text")
finally:
    print("Program Finished")


# Use else — print result only if no error occurred
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ZeroDivisionError:
    print("The denominator cannot be 0")
except ValueError:
    print("Enter a number not text")
else:
    print(result)