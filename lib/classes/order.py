
class Order:

    all = []

    def __init__(self, customer, coffee, price = 0):
        self.customer = customer
        self.coffee = coffee
        self.set_price(price)
        Order.all.append(self)
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if (type(price) is int) and (1 <= price <= 10):
            self._price = price
        else:
            raise Exception("Price must be a number between 1 and 10!")
    
    price = property(get_price, set_price)
