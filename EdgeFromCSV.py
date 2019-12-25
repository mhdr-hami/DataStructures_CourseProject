import pandas as pd
from OwnershipEdge import *
from TransactionEdge import *
from RelationEdge import *
from CallEdge import *
from NodeFromCSV import *
########################################################################################################################

#Ownerships
df_ownerships = pd.read_csv('data/ownerships.csv')
ownerShipsDictionary = {}
for i in range(len(df_ownerships)):
    ownership_tmp = OwnershipEdge(df_ownerships.iloc[i][2], df_ownerships.iloc[i][0], df_ownerships.iloc[i][1], df_ownerships.iloc[i][3], df_ownerships.iloc[i][4])
    ownerShipsDictionary[df_ownerships.iloc[i][2]] = ownership_tmp
for key in ownerShipsDictionary:
    personDictionary[ownerShipsDictionary[key].FromNode].outgoing.append(ownerShipsDictionary[key])
    personDictionary[ownerShipsDictionary[key].ToNode].incomming.append(ownerShipsDictionary[key])

########################################################################################################################

#Calls
df_calls = pd.read_csv('data/calls.csv')
callsDictionary = {}
for i in range(len(df_calls)):
    call_tmp = CallEdge(df_calls.iloc[i][2], df_calls.iloc[i][0], df_calls.iloc[i][1], df_calls.iloc[i][3], df_calls.iloc[i][4])
    callsDictionary[df_calls.iloc[i][2]] = call_tmp
for key in callsDictionary:
    personDictionary[callsDictionary[key].FromNode].outgoing.append(callsDictionary[key])
    personDictionary[callsDictionary[key].ToNode].incomming.append(callsDictionary[key])

########################################################################################################################

#Transactions
df_transactions = pd.read_csv('data/transactions.csv')
transactionsDictionary = {}
for i in range(len(df_transactions)):
    transaction_tmp = TransactionEdge(df_transactions.iloc[i][2], df_transactions.iloc[i][0], df_transactions.iloc[i][1], df_transactions.iloc[i][3], df_transactions.iloc[i][4])
    transactionsDictionary[df_transactions.iloc[i][2]] = transaction_tmp
for key in transactionsDictionary:
    personDictionary[transactionsDictionary[key].FromNode].outgoing.append(transactionsDictionary[key])
    personDictionary[transactionsDictionary[key].ToNode].incomming.append(transactionsDictionary[key])

########################################################################################################################

#Relations
df_relations = pd.read_csv('data/relationships.csv')
relationsDictionary = {}
for i in range(len(df_relations)):
    x = str(df_relations.iloc[i][0]) + str(df_relations.iloc[i][1])
    relation_tmp = RelationEdge(x, df_relations.iloc[i][0], df_relations.iloc[i][1], df_relations.iloc[i][2], df_relations.iloc[i][3])
    relationsDictionary[x] = relation_tmp
for key in relationsDictionary:
    personDictionary[relationsDictionary[key].FromNode].outgoing.append(relationsDictionary[key])
    personDictionary[relationsDictionary[key].ToNode].incomming.append(relationsDictionary[key])
