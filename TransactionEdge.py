from Edge import *


class TransactionEdge(Edge):
    def __init__(self, FromNode, ToNode, TransactionID, Amount, Date):
        self.FromNode = FromNode
        self.ToNode = ToNode
        self.UniqueKey = TransactionID
        self.Amount = Amount
        self.Date = Date

