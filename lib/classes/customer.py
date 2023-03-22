# from classes.order import Order

# class Customer:
#     def __init__(self, name):
#         self.set_name(name)

#     def get_name(self):
#         return self._name

#     def set_name(self, name):
#         if (type(name) is str) and (1 <= len(name) <= 15):
#             self._name = name
#             self.customer_order_list = []
#             self.coffee_order_list = []
#         else:
#             raise Exception("Name must be string between 1 and 15!")

#     name = property(get_name, set_name)

#     def orders(self):
#         self.customer_order_list = []
#         for order in Order.all:
#             if order.customer == self:
#                 self.customer_order_list.append(order)
#         return self.customer_order_list
    
#     def coffees(self):
#         self.customer_order_list = []
#         self.orders()
#         self.coffee_order_list = []
#         for order in self.customer_order_list:
#             if order.coffee not in self.coffee_order_list:
#                 self.coffee_order_list.append(order.coffee)
#         return self.coffee_order_list
    
#     def create_order(self,coffee,price):
#         Order(self, coffee, price)



## David's Way ##

from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    def set_name(self,input):
        if type(input) is str and len(input) > 0 and len(input) < 16:
                self._name = input
        else:
            raise Exception("Not valid name")
    name = property(get_name,set_name)

    def orders(self):
        from .order import Order
        orderlist = []
        for order in Order.all:
            if order.customer == self:
                orderlist.append(order)
        return orderlist

    def coffees(self):
        from .order import Order
        coffeeslist = []
        for order in Order.all:
            if order.customer == self:
                if order.coffee not in coffeeslist:
                    coffeeslist.append(order.coffee)
        return coffeeslist
    
    def create_order(self,coffee,price):
        from .order import Order
        from .coffee import Coffee
        if type(coffee) is Coffee and type(price) is int:
            Order(self,coffee,price)
        else:
            raise Exception("Not valid inputs")