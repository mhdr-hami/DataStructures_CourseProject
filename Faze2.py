from EdgeFromCSV import *
# runpy.run_path('EdgeFromCSV.py')

########################################################################################################################

fazeTwoSuspected = []
for key in personDictionary:
    suspected = {}
    if personDictionary[key].job == "گمرک" or personDictionary[key].job == "سازمان بنادر":
        for item in personDictionary[key].outgoing:
            if item[1] == "relation":
                suspected[relationsDictionary[str(item[0])].toNode] = 1

    for sPerson in suspected:
        for key2 in personDictionary[str(sPerson)].outgoing:
            if key2[1] == "ownerShip":
                x = list(str(ownerShipsDictionary[key2[0]].buyDate).split("-"))

                if 2020 * 365 - int(x[0]) * 365 + int(x[1]) * 30 + int(x[2]) < 365 * 2:
                    if key not in fazeTwoSuspected:
                        fazeTwoSuspected.append(key)
# for key in fazeTwoSuspected:
#     print(personDictionary[key].unique_Key)
########################################################################################################################