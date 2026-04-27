class phone:
    def __init__(self,model,price):
        self.model=model
        self.price=price
    
    def information(self):
        print(f"This is {self.model} and its price is {self.price}")

phone_one=phone("redmi c55","Rs.20,000")
phone_one.information()