from EdgeFromCSV import *
runpy.run_path('EdgeFromCSV.py')

########################################################################################################################

fazeTwoSuspected = []
for key in personDictionary:
    suspected = {}
    if personDictionary[key].job == "گمرک":
        checkingNodes = []
        for item in personDictionary[key].outgoing:
            if item[1] == "relation":
                checkingNodes.append(relationsDictionary[str(item[0])].toNode)
                suspected[relationsDictionary[str(item[0])].toNode] = 1
        maxDist = 1
        while maxDist <= 5 and len(checkingNodes) != 0:
            topNodeKey = checkingNodes[0]
            topNode = personDictionary[str(topNodeKey)]
            checkingNodes.pop()
            for item in topNode.outgoing:
                if item[1] == "relation" and relationsDictionary[str(item[0])].fromNode not in suspected:
                    checkingNodes.append(relationsDictionary[str(item[0])].toNode)
                    suspected[relationsDictionary[str(item[0])].toNode] = suspected[topNodeKey] + 1
                    maxDist = suspected[topNodeKey] + 1
    for sPerson in suspected:
        for key2 in personDictionary[str(sPerson)].outgoing:
            if key2[1] == "ownerShip":
                x = list(str(ownerShipsDictionary[key2[0]].buyDate).split("-"))
                # if ownerShipsDictionary[key2[0]].fromNode == personDictionary[str(sPerson)].unique_Key and 2020 * 365 - int(x[0]) * 365 + int(x[1]) * 30 + int(x[2]) < 365 * 2:
                if 2020 * 365 - int(x[0]) * 365 + int(x[1]) * 30 + int(x[2]) < 365 * 2:
                    if key not in fazeTwoSuspected:
                        fazeTwoSuspected.append(key)
                    # print(personDictionary[key].unique_Key, personDictionary[key].job, ownerShipsDictionary[key2[0]].buyDate, ownerShipsDictionary[key2[0]].fromNode)
########################################################################################################################