from Faze2 import *
runpy.run_path("Faze2.py")

########################################################################################################################
fazeThreeSuspected = []
for sPerson in fazeTwoSuspected:
    visited = {}
    checkingNodes = []
    for item in personDictionary[sPerson].incomming:
        if item[1] == "transaction":
            checkingNodes.append(bankAccDictionary[transactionsDictionary[str(item[0])].fromNode].idNumber)
            visited[bankAccDictionary[transactionsDictionary[str(item[0])].fromNode].idNumber] = [1, transactionsDictionary[str(item[0])].date, transactionsDictionary[str(item[0])].amount, transactionsDictionary[str(item[0])].uniqueKey]
            if personDictionary[str(bankAccDictionary[transactionsDictionary[str(item[0])].fromNode].idNumber)].job == "قاچاقچی":
                fazeThreeSuspected.append(sPerson)
    maxDist = 1
    while maxDist <= 5 and len(checkingNodes) != 0:
        topNodeKey = checkingNodes[0]
        topNode = personDictionary[topNodeKey]
        checkingNodes.pop()
        for item in topNode.incomming:
            if item[1] == "transaction" and bankAccDictionary[transactionsDictionary[str(item[0])].fromNode].idNumber not in visited:
                x = list(str(transactionsDictionary[str(item[0])].date).split("-"))
                intx = 365 * int(x[0]) + 30 * int(x[1]) + int(x[2])
                x2 = list(str(visited[topNodeKey][1]).split("-"))
                intx2 = 365 * int(x2[0]) + 30 * int(x2[1]) + int(x2[2])
                y = int(transactionsDictionary[str(item[0])].amount)
                y2 = int(visited[topNodeKey][3])
                if intx > intx2 and y < y2:
                    checkingNodes.append(transactionsDictionary[str(item[0])].toNode)
                    visited[transactionsDictionary[str(item[0])].toNode] = [visited[topNodeKey][0]+1, transactionsDictionary[str(item[0])].date, transactionsDictionary[str(item[0])].amount, transactionsDictionary[str(item[0])].uniqueKey]
                    maxDist = visited[topNodeKey][0]+1
                    if personDictionary[transactionsDictionary[str(item[0])].toNode].job == "قاچاقچی":
                        if sPerson not in fazeThreeSuspected:
                            fazeThreeSuspected.append(sPerson)
for key in fazeThreeSuspected:
    print(personDictionary[key].unique_Key)