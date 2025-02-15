


class Product():
    def __init__(self, name, price, quantity):
        if name == '':
            raise ValueError("Invalid input, Product must have a name")
        if price < 0:
            raise ValueError("Invalid input, Price cannot be negative")
        if quantity < 0:
            raise ValueError("Invalid input, Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self):
        if self.active:
            return True
        else:
            return False

    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'


    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError("Error while making order! Quantity larger than what exists")
        self.set_quantity(self.quantity - quantity)
        return quantity * self.price


try:
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
except ValueError as e:
    bose = None
    print(e)
try:
    mac = Product("MacBook Air M2", price=1450, quantity=100)
except ValueError as e:
    mac = None
    print(e)

try:
    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())
    print(bose.show())
    print(mac.show())
    bose.set_quantity(1000)
    print(bose.show())
except AttributeError as e:
    print(e)
