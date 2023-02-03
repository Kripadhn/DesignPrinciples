Each object should only talk to its immediate neighbors.

Example: A class that implements a shopping cart, and a class that implements a payment service.

class PaymentService:
    def process_payment(self, amount):
        # code to process payment
        pass

class ShoppingCart:
    def __init__(self, payment_service):
        self.payment_service = payment_service
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def checkout(self):
        total_amount = sum(item.price for item in self.items)
        self.payment_service.process_payment(total_amount)

# In this example, the ShoppingCart class only communicates with its PaymentService instance, and does not access the inner workings of the PaymentService class. 
This helps to minimize coupling and make the system more maintainable and scalable.