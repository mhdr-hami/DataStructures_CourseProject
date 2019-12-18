from Node import *


class HouseNode(Node):
    def __init__(self, zipCode, idNumber, price, area, address):
        self.unique_Key = zipCode
        self.idNumber = idNumber
        self.price = price
        self.area = area
        self.address = address
