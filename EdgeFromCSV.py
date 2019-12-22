import pandas as pd
from OwnershipEdge import *
from TransactionEdge import *
from RelationEdge import *
from CallEdge import *
########################################################################################################################

#Ownerships
df_ownerships = pd.read_csv('data/ownerships.csv')
df_ownerships = df_ownerships[[df_ownerships.columns[2], df_ownerships.columns[0], df_ownerships.columns[1], df_ownerships.columns[3], df_ownerships.columns[4]]]
ownerShipsDictionary = {}
for i in range(len(df_ownerships)):
    ownership_tmp = OwnershipEdge(df_ownerships.iloc[i][0], df_ownerships.iloc[i][1], df_ownerships.iloc[i][2], df_ownerships.iloc[i][3], df_ownerships.iloc[i][4])
    ownerShipsDictionary[df_ownerships.iloc[i][0]] = ownership_tmp

########################################################################################################################

#Calls
df_calls = pd.read_csv('data/calls.csv')
df_calls = df_calls[[df_calls.columns[2], df_calls.columns[0], df_calls.columns[1], df_calls.columns[3], df_calls.columns[4]]]
callsDictionary = {}
for i in range(len(df_calls)):
    call_tmp = CallEdge(df_calls.iloc[i][0], df_calls.iloc[i][1], df_calls.iloc[i][2], df_calls.iloc[i][3], df_calls.iloc[i][4])
    callsDictionary[df_calls.iloc[i][0]] = call_tmp

########################################################################################################################

