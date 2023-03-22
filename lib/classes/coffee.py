# from classes.order import Order

# class Coffee:
#     def __init__(self, name):
#         self.set_name(name)
        
#     def get_name(self):
#         return self._name
    
#     def set_name(self, name):
#         if hasattr(self, "_name"):
#             raise Exception("Cannot change Coffee Name!")
#         elif (type(name) is not str):
#             raise Exception("Name must be a string!")
#         else:
#             self._name = name
#             self.coffee_order_list = []
#             self.customer_order_list = []

#     name = property(get_name, set_name)

#     def orders(self):
#         self.coffee_order_list = []
#         for order in Order.all:
#             if order.coffee == self:
#                 self.coffee_order_list.append(order)
#         return self.coffee_order_list
    
#     def customers(self):
#         self.coffee_order_list = []
#         self.orders()
#         self.customer_order_list = []
#         for order in self.coffee_order_list:
#             if order.customer not in self.customer_order_list:
#                 self.customer_order_list.append(order.customer)
#         return self.customer_order_list
    
#     def num_orders(self):
#         self.orders()
#         return len(self.coffee_order_list)
    
#     def average_price(self):
#         self.orders()
#         total_price = 0
#         order_num = 0
#         for order in self.coffee_order_list:
#             if order.coffee == self:
#                 total_price += order.price
#                 order_num += 1
#         if order_num != 0:
#             avg_price = total_price / order_num
#             return avg_price



## David's Way ##
    
from classes.order import Order

class Coffee:
    def __init__(self, name):
        if type(name) is str:
            self._name = name
        self.uniquecus = []
    def get_name(self):
        return self._name
    def set_name(self,input):
        raise Exception("Can't change name")
    name = property(get_name,set_name)

    def orders(self):
        from .order import Order
        orderlist = []
        for order in Order.all:
            if order.coffee == self:
                orderlist.append(order)
        return orderlist
    
    def customers(self):
        return self.uniquecus

    def num_orders(self):
        from .order import Order
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    def average_price(self):
        from .order import Order
        totalprice = 0
        count = 0
        for order in Order.all:
            if order.coffee == self:
                totalprice += order.price
                count += 1
        return totalprice/count