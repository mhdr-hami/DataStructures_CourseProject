from Edge import *


class TransactionEdge(Edge):
    def __init__(self, transactionID, fromNode, toNode, date, amount):
        self.fromNode = fromNode
        self.toNode = toNode
        self.uniqueKey = transactionID
        self.amount = amount
        self.date = date

