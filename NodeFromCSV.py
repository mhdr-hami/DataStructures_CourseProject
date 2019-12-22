import pandas as pd
from PersonNode import *
from CarNode import *
from PhoneNumberNode import *
from HouseNode import *
from BankAccount import *
########################################################################################################################

# CARS
df_cars = pd.read_csv('data/cars.csv')
carsDictionary = {}
for i in range(len(df_cars)):
    car_tmp = CarNode(df_cars.iloc[i][0], df_cars.iloc[i][1], df_cars.iloc[i][2], df_cars.iloc[i][3])
    carsDictionary[df_cars.iloc[i][0]] = car_tmp

########################################################################################################################

# Houses
df_houses = pd.read_csv('data/homes.csv')
houseDictionary = {}
for i in range(len(df_houses)):
    house_tmp = HouseNode(df_houses.iloc[i][2], df_houses.iloc[i][1], df_houses.iloc[i][0], df_houses.iloc[i][3], df_houses.iloc[i][4])
    houseDictionary[df_houses.iloc[i][2]] = house_tmp

########################################################################################################################

# BankAccount
df_bankAccounts = pd.read_csv('data/accounts.csv')
bankDictionary = {}
for i in range(len(df_bankAccounts)):
    bank_tmp = BankAccount(df_bankAccounts.iloc[i][2], df_bankAccounts.iloc[i][1], df_bankAccounts.iloc[i][0], df_bankAccounts.iloc[i][3])
    bankDictionary[df_bankAccounts.iloc[i][2]] = bank_tmp

########################################################################################################################

# Persons
df_persons = pd.read_csv('data/people.csv')
personDictionary = {}
for i in range(len(df_persons)):
    person_tmp = PersonNode(df_persons.iloc[i][2], df_persons.iloc[i][1], df_persons.iloc[i][0], df_persons.iloc[i][3], df_persons.iloc[i][4], df_persons.iloc[i][5], df_persons.iloc[i][6])
    personDictionary[df_persons.iloc[i][2]] = person_tmp

########################################################################################################################

# PhoneNumbers
df_phoneNumbers = pd.read_csv('data/phones.csv')
phonesDictionary = {}
for i in range(len(df_phoneNumbers)):
    phone_tmp = PhoneNumberNode(df_phoneNumbers.iloc[i][1], df_phoneNumbers.iloc[i][0], df_phoneNumbers.iloc[i][2])
    phonesDictionary[df_phoneNumbers.iloc[i][1]] = phone_tmp



