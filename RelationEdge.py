from Edge import *


class RelationEdge(Edge):
    def __init__(self, FromNode, ToNode, Relation, Beginning):
        self.FromNode = FromNode
        self.ToNode = ToNode
        self.UniqueKey = 0
        self.Relation = Relation
        self.Beginning = Beginning
