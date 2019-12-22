import pandas as pd
from OwnershipEdge import *
from TransactionEdge import *
from RelationEdge import *
from CallEdge import *
########################################################################################################################

#Ownerships
df_ownerships = pd.read_csv('data/ownerships.csv')
ownerShipsDictionary = {}
for i in range(len(df_ownerships)):
    ownership_tmp = OwnershipEdge(df_ownerships.iloc[i][2], df_ownerships.iloc[i][0], df_ownerships.iloc[i][1], df_ownerships.iloc[i][3], df_ownerships.iloc[i][4])
    ownerShipsDictionary[df_ownerships.iloc[i][2]] = ownership_tmp

########################################################################################################################

#Calls
df_calls = pd.read_csv('data/calls.csv')
callsDictionary = {}
for i in range(len(df_calls)):
    call_tmp = CallEdge(df_calls.iloc[i][2], df_calls.iloc[i][0], df_calls.iloc[i][1], df_calls.iloc[i][3], df_calls.iloc[i][4])
    callsDictionary[df_calls.iloc[i][2]] = call_tmp

########################################################################################################################

#Transactions
df_transactions = pd.read_csv('data/transactions.csv')
transactionsDictionary = {}
for i in range(len(df_transactions)):
    transaction_tmp = TransactionEdge(df_transactions.iloc[i][2], df_transactions.iloc[i][0], df_transactions.iloc[i][1], df_transactions.iloc[i][3], df_transactions.iloc[i][4])
    transactionsDictionary[df_transactions.iloc[i][2]] = transaction_tmp

########################################################################################################################

#Relations
df_relations = pd.read_csv('data/relationships.csv')
relationsDictionary = {}
for i in range(len(df_relations)):
    x = str(df_relations.iloc[i][0]) + str(df_relations.iloc[i][1])
    relation_tmp = RelationEdge(x, df_relations.iloc[i][0], df_relations.iloc[i][1], df_relations.iloc[i][2], df_relations.iloc[i][3])
    relationsDictionary[x] = relation_tmp