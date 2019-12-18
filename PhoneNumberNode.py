from Node import *


class PhoneNumberNode(Node):
    def __init__(self, cimNumber, idNumber, operatorName):
        self.unique_Key = cimNumber
        self.idNumber = idNumber
        self.operatorName = operatorName


