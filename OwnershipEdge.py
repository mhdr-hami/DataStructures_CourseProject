from Edge import *


class OwnershipEdge(Edge):
    def __init__(self, FromNode, ToNode, SAID , BuyDate, Price):
        self.FromNode = FromNode
        self.ToNode = ToNode
        self.UniqueKey = SAID
        self.BuyDate = BuyDate
        self.Price = Price
