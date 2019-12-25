from Edge import *


class OwnershipEdge(Edge):
    def __init__(self, SAID, fromNode, toNode, buyDate, price):
        self.fromNode = fromNode
        self.toNode = toNode
        self.uniqueKey = SAID
        self.buyDate = buyDate
        self.price = price
