# class Order:

#     all = []

#     def __init__(self, customer, coffee, price = 0):
#         self.customer = customer
#         self.coffee = coffee
#         self.set_price(price)
#         Order.all.append(self)
    
#     def get_price(self):
#         return self._price
    
#     def set_price(self, price):
#         if (type(price) is int) and (1 <= price <= 10):
#             self._price = price
#         else:
#             raise Exception("Price must be a number between 1 and 10!")
    
#     price = property(get_price, set_price)



## David's Way ##


class Order:
    all = []
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        if customer not in coffee.uniquecus:
            coffee.uniquecus.append(customer)
        Order.all.append(self)
    def get_price(self):
        return self._price
    def set_price(self,input):
        if type(input) is int and input > 0 and input<=10:
            self._price = input
        else:
            raise Exception("Not valid price")
    price = property(get_price,set_price)

    def get_customer(self):
        return self._customer
    def set_customer(self,input):
        from .customer import Customer
        if type(input) is Customer:
            self._customer = input
        else:
            raise Exception("Not valid customer")
    customer = property(get_customer,set_customer)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self,input):
        from .coffee import Coffee
        if type(input) is Coffee:
            self._coffee = input
        else:
            raise Exception("Not valid customer")
    coffee = property(get_coffee,set_coffee)