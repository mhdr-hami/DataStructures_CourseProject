from OwnershipEdge import *
from TransactionEdge import *
from RelationEdge import *
from CallEdge import *
from NodeFromCSV import *
import runpy
runpy.run_path('NodeFromCSV.py')
########################################################################################################################

#Ownerships
df_ownerships = pd.read_csv('data/ownerships.csv')
ownerShipsDictionary = {}
for i in range(len(df_ownerships)):
    ownership_tmp = OwnershipEdge(df_ownerships.iloc[i][2], df_ownerships.iloc[i][0], df_ownerships.iloc[i][1], df_ownerships.iloc[i][3], df_ownerships.iloc[i][4])
    ownerShipsDictionary[df_ownerships.iloc[i][2]] = ownership_tmp
for key in ownerShipsDictionary:
    tmp_list = [key, "ownerShip"]
    personDictionary[str(ownerShipsDictionary[key].fromNode)].outgoing.append(tmp_list)

########################################################################################################################

#Calls
df_calls = pd.read_csv('data/calls.csv')
callsDictionary = {}
for i in range(len(df_calls)):
    call_tmp = CallEdge(df_calls.iloc[i][2], df_calls.iloc[i][0], df_calls.iloc[i][1], df_calls.iloc[i][3], df_calls.iloc[i][4])
    callsDictionary[df_calls.iloc[i][2]] = call_tmp
for key in callsDictionary:
    tmp_list = [key, "call"]
    personDictionary[str(phonesDictionary[str(callsDictionary[key].fromNode)].idNumber)].outgoing.append(tmp_list)
    personDictionary[str(phonesDictionary[str(callsDictionary[key].toNode)].idNumber)].incomming.append(tmp_list)

########################################################################################################################

#Transactions
df_transactions = pd.read_csv('data/transactions.csv')
transactionsDictionary = {}
for i in range(len(df_transactions)):
    transaction_tmp = TransactionEdge(df_transactions.iloc[i][2], df_transactions.iloc[i][0], df_transactions.iloc[i][1], df_transactions.iloc[i][3], df_transactions.iloc[i][4])
    transactionsDictionary[str(df_transactions.iloc[i][2])] = transaction_tmp
for key in transactionsDictionary:
    tmp_list = [key, "transaction"]
    personDictionary[str(bankAccDictionary[str(transactionsDictionary[key].fromNode)].idNumber)].outgoing.append(tmp_list)
    personDictionary[str(bankAccDictionary[str(transactionsDictionary[key].toNode)].idNumber)].incomming.append(tmp_list)

########################################################################################################################

#Relations
df_relations = pd.read_csv('data/relationships.csv')
relationsDictionary = {}
for i in range(len(df_relations)):
    x = str(df_relations.iloc[i][0]) + str(df_relations.iloc[i][1])
    relation_tmp = RelationEdge(x, df_relations.iloc[i][0], df_relations.iloc[i][1], df_relations.iloc[i][2], df_relations.iloc[i][3])
    relationsDictionary[x] = relation_tmp
for key in relationsDictionary:
    tmp_list = [key, "relation"]
    personDictionary[str(relationsDictionary[key].fromNode)].outgoing.append(tmp_list)
    personDictionary[str(relationsDictionary[key].toNode)].incomming.append(tmp_list)

########################################################################################################################

#faze2
for key in personDictionary:
    if personDictionary[key].job == "گمرک":
        checkingNode = []
        maznoon = []
        for item in personDictionary[key].outgoing:
            if item[1] == "relation":
                checkingNode.append(relationsDictionary[str(item[0])].toNode)
                maznoon.append(relationsDictionary[str(item[0])].toNode)
        maxDist = 1
        while maxDist <= 5:
            nodeForCheck = checkingNode[0]
            checkingNode.pop()
            for item in nodeForCheck.outgoing:
                if item[1] == "relation" and !(item[0] in maznoon):
                    checkingNode.append(relationsDictionary[str(item[0])].toNode)
                    maznoon.append(relationsDictionary[str(item[0])].toNode)
                    maxDist += 1
    for item in maznoon:
        for key2 in ownerShipsDictionary:
            if ownerShipsDictionary[key].fromNode == item.idNumber and ownerShipsDictionary[key].buyDate<"2 sal":
                print(personDictionary[key])
