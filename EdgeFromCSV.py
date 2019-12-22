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
