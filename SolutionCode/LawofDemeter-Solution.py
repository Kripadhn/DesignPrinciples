class Order:
    def __init__(self, customer):
        self.customer = customer

class Customer:
    def __init__(self, address):
        self.address = address

class Address:
    def __init__(self, street):
        self.street = street

address = Address("123 Main St.")
customer = Customer(address)
order = Order(customer)
print(order.customer.address.street) # 123 Main St.
