try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ZeroDivisionError:
    print("The denominator cannot be 0")
except ValueError:
    print("Enter a number not text")
else:
    print(result)