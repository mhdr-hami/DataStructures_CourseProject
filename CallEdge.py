from Edge import *


class CallEdge(Edge):
    def __init__(self, CallId, FromNode, ToNode, Date, Duration):
        self.FromNode = FromNode
        self.ToNode = ToNode
        self.UniqueKey = CallId
        self.Date = Date
        self.Duration = Duration
