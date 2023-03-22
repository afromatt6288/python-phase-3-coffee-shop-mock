#!/usr/bin/env python3
# import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

coffee = Coffee("Peppermint Mocha")
# with pytest.raises(Exception):
coffee.name = 'Banana'
    # ipdb.set_trace()
