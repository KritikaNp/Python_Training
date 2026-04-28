class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def information(self):
        print(f"{self.brand} {self.model} costs Rs.{self.price}")
    
    def discount(self, percent):
        discounted = self.price - (self.price * percent / 100)
        print(f"After {percent}% discount: Rs.{discounted}")

phone1 = Phone("Redmi", "C55", 20000)
phone1.information()
phone1.discount(10)