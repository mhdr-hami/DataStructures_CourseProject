from Node import *


class BankAccount(Node):
    def __init__(self, shabaNumber, idNumber, bankName, accountNumber):
        self.unique_Key = shabaNumber
        self.idNumber = idNumber
        self.bankName = bankName
        self.accountNumber = accountNumber
