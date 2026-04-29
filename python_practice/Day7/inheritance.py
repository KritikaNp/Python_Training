# Inheritance Q1
class Animal():
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print(f"{self.name} makes a sound")
    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")

dog=Dog("Bruno")
dog.speak()

cat=Cat("Ferguson")
cat.speak()

# Create:

# Parent class Vehicle with brand and speed
# Child class Car that adds number of doors
# Child class Bike that adds type (mountain/road)
class Vehicle():
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed
    
    def info(self):
        print(f"{self.brand} has speed of {self.speed} km/hr")
class Car(Vehicle):
    def doors(self):
        print(f"{self.brand} has 4 doors")

class Bike(Vehicle):
    def type(self,terrain):
        if terrain=="pavement":
            print(f"{self.brand} is a Road bike")
        else:
            print(f"{self.brand} is a mountain bike")

car=Car("Honda",70)
car.info()
car.doors()

bike=Bike("Schwinn",80)
bike.info()
bike.type("not pavement")

