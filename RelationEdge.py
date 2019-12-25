from Edge import *


class RelationEdge(Edge):
    def __init__(self, uniqueKey, fromNode, toNode, relation, beginning):
        self.fromNode = fromNode
        self.toNode = toNode
        self.uniqueKey = uniqueKey
        self.relation = relation
        self.beginning = beginning
