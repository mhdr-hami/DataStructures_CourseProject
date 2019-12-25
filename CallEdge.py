from Edge import *


class CallEdge(Edge):
    def __init__(self, callId, fromNode, toNode, date, duration):

        self.fromNode = fromNode
        self.toNode = toNode
        self.uniqueKey = callId
        self.date = date
        self.duration = duration
