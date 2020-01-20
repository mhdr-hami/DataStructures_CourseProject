from Faze3 import *
fazeFourSuspected = []
for key in fazeThreeSuspected:
    edges = personDictionary[key].incomming + personDictionary[key].outgoing
    for item in edges:
        if item[1] == "call":
            phone1 = phonesDictionary[str(callsDictionary[item[0]].toNode)]
            phone2 = phonesDictionary[str(callsDictionary[item[0]].fromNode)]
            if personDictionary[str(phone1.idNumber)].job == "قاچاقچی" or personDictionary[str(phone2.idNumber)].job == "قاچاقچی":
                if key not in fazeFourSuspected:
                    fazeFourSuspected.append(key)

print(len(fazeTwoSuspected))
print(len(fazeThreeSuspected))
print(len(fazeFourSuspected))
for key in fazeThreeSuspected:
    print(personDictionary[key].name, personDictionary[key].familyName, sep=" ")
for i in list_of_paths:
    for j in i:
        print(personDictionary[str(j)].name, personDictionary[str(j)].familyName ,personDictionary[str(j)].job, sep=":")