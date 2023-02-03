class Order:
    def __init__(self):
        self.customer = Customer()

class Customer:
    def __init__(self):
        self.address = Address()

class Address:
    def __init__(self):
        self.street = "123 Main St."

order = Order()
print(order.customer.address.street) # 123 Main St.
