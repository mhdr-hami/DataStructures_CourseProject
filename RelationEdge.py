from Edge import *


class RelationEdge(Edge):
    def __init__(self, uniqueKey, FromNode, ToNode, Relation, Beginning):
        self.FromNode = FromNode
        self.ToNode = ToNode
        self.UniqueKey = uniqueKey
        self.Relation = Relation
        self.Beginning = Beginning
