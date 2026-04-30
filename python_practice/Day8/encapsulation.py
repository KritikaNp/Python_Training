class BankAccount:
    def __init__(self,balance):
        self.__balance=balance # __balance makes it private variable
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance") 
        else:
            self.__balance-=amount
    def get_balance(self):
        print(f"your balance is {self.__balance}")
    
Account=BankAccount(1000)
Account.deposit(600)
Account.withdraw(300)
Account.get_balance()
# print(Account.__balance)  this is error cannot access private variable outside the class


# Create a Student class with:

# private __grade attribute
# method to set grade with validation (only 0-100)
# method to get grade

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.__grade=grade
    
    def set_grade(self, new_grade):
        if new_grade>100 or new_grade<0:
            print("The grade should be from 0 to 100")
        else:
            self.__grade=new_grade
            print(f"Grade updated to {self.__grade}")
    def get_grade(self):
        print(f"Your grade is {self.__grade}")

stu=Student("Kritika",84)
stu.set_grade(98)
stu.get_grade()