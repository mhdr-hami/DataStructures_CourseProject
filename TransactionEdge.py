from Edge import *


class TransactionEdge(Edge):
    def __init__(self, TransactionID, FromNode, ToNode, Date, Amount):
        self.FromNode = FromNode
        self.ToNode = ToNode
        self.UniqueKey = TransactionID
        self.Amount = Amount
        self.Date = Date

