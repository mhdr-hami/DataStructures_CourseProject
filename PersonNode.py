from Node import *


class PersonNode (Node):
    def __init__(self, idNumber, name, familyName, birthDay, birthPlace, jobPlace):
        self.unique_Key = idNumber
        self.name = name
        self.familyName = familyName
        self.birthDay = birthDay
        self.birthPlace = birthPlace
        self.jobPlace = jobPlace
#hello

