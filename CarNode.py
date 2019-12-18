from Node import *


class CarNode(Node):
    def __init__(self, numberplate, idNumber, model, color):
        self.unique_Key = numberplate
        self.idNumber = idNumber
        self.model = model
        self.color = color

