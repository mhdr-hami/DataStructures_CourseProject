from Faze2 import *
# runpy.run_path("Faze2.py")

########################################################################################################################
fazeThreeSuspected = []
list_of_paths = []

# i = 0
for sPerson in fazeTwoSuspected:
    flag = 0
    visited = {}
    checkingNodes = []
    for item in personDictionary[sPerson].incomming:
        if item[1] == "transaction":
            theNODE = bankAccDictionary[str(transactionsDictionary[str(item[0])].fromNode)].idNumber
            checkingNodes.append(theNODE)
            visited[theNODE] = [1, transactionsDictionary[str(item[0])].date, transactionsDictionary[str(item[0])].amount, transactionsDictionary[str(item[0])].uniqueKey, [sPerson, theNODE]]
            if personDictionary[str(theNODE)].job == "قاچاقچی":
                fazeThreeSuspected.append(sPerson)
                list_of_paths.append(visited[theNODE][4])
                flag = 1
                break
    if flag == 1:
        continue
    maxDist = 1
    while maxDist <= 5 and len(checkingNodes) != 0:
        topNodeKey = checkingNodes[0]
        topNode = personDictionary[str(topNodeKey)]
        checkingNodes.pop(0)
        for item in topNode.incomming:
            if item[1] == "transaction":
                theNODE = bankAccDictionary[str(transactionsDictionary[str(item[0])].fromNode)].idNumber
                if theNODE not in visited or (theNODE in visited and visited[theNODE][3] != item[0]):
                    x = list(str(transactionsDictionary[str(item[0])].date).split("-"))
                    intx = 365 * int(x[0]) + 30 * int(x[1]) + int(x[2])
                    x2 = list(str(visited[topNodeKey][1]).split("-"))
                    intx2 = 365 * int(x2[0]) + 30 * int(x2[1]) + int(x2[2])
                    y = int(transactionsDictionary[str(item[0])].amount)
                    y2 = int(visited[topNodeKey][3])
                    if intx < intx2 and y > y2:
                        checkingNodes.append(theNODE)
                        path = visited[topNodeKey][4]
                        path.append(theNODE)
                        visited[theNODE] = [visited[topNodeKey][0]+1, transactionsDictionary[str(item[0])].date, transactionsDictionary[str(item[0])].amount, transactionsDictionary[str(item[0])].uniqueKey, path]
                        if personDictionary[str(theNODE)].job == "قاچاقچی":
                            if sPerson not in fazeThreeSuspected:
                                fazeThreeSuspected.append(sPerson)
                                list_of_paths.append(visited[theNODE][4])
                                flag = 1
                                break
                        maxDist = visited[topNodeKey][0] + 1
            if flag == 1:
                break
        if flag == 1:
            break

