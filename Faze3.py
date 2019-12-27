from Faze2 import *
runpy.run_path("Faze2.py")

########################################################################################################################
fazeThreeSuspected = []
for sPerson in fazeTwoSuspected:
    visited = {}
    checkingNodes = []
    for item in personDictionary[sPerson].outgoing:
        if item[1] == "relation":
            checkingNodes.append(relationsDictionary[item[0]].toNode)
            visited[relationsDictionary[item[0]].toNode] = 1
    maxDist = 1
    while maxDist <= 5 and len(checkingNodes) != 0:
        topNodeKey = checkingNodes[0]
        topNode = personDictionary[topNodeKey]
        checkingNodes.pop()
        for item in topNode.outgoing:
            if item[1] == "relation" and not relationsDictionary[str(item[0])].fromNode in visited:
                checkingNodes.append(relationsDictionary[str(item[0])].fromNode)