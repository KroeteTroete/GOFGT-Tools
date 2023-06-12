#This script was used to create the spreadsheet for the "generic" fsb
import pandas
import os
from os.path import isfile, join

# Spalten:
#     line: transcribed line
#     file: voice line file name
#     faction: which faction voice is used
#     gender: which gender is used

genericpath = "assets/generic/"
dupl1path = f"{genericpath}/dupl/"
dupl2path = f"{genericpath}/dupl2/"
dupl3path = f"{genericpath}/dupl3/"
dupl4path = f"{genericpath}/dupl4/"
dupl5path = f"{genericpath}/dupl5/"

line = []
file = []
faction = []
gender = []
isdupl = []
inlang = []

#iterator = []

spalten = [line,file,faction,gender,isdupl]

# for i in range(0, 130):
#     iterator.append(str(i))

for i in range(0, 130):
    line.append("EMPTY")

for i in range(0, 130):
    isdupl.append("None")

for i in os.listdir(genericpath):
    if isfile(join(genericpath, i)):
        file.append(i)
        # print(len(file))

for i in range(0, 130):
    faction.append("EMPTY")

for i in range(0, 130):
    gender.append("EMPTY")

#dupl loops
for i in os.listdir(dupl1path):
    if isfile(join(dupl1path, i)):
        file.append(i)
        isdupl.append("dupl1")
        line.append("Empty")
        faction.append("Empty")
        gender.append("Empty")
        #iterator.append(str(len(iterator) + 1))
        print(len(file))

for i in os.listdir(dupl2path):
    if isfile(join(dupl2path, i)):
        file.append(i)
        isdupl.append("dupl2")
        line.append("Empty")
        faction.append("Empty")
        gender.append("Empty")
        #iterator.append(str(len(iterator) + 1))
        print(len(file))


for i in os.listdir(dupl3path):
    if isfile(join(dupl3path, i)):
        file.append(i)
        isdupl.append("dupl3")
        line.append("Empty")
        faction.append("Empty")
        gender.append("Empty")
        #iterator.append(str(len(iterator) + 1))
        print(len(file))

for i in os.listdir(dupl4path):
    if isfile(join(dupl4path, i)):
        file.append(i)
        isdupl.append("dupl4")
        line.append("Empty")
        faction.append("Empty")
        gender.append("Empty")
        #iterator.append(str(len(iterator) + 1))
        print(len(file))

for i in os.listdir(dupl5path):
    if isfile(join(dupl5path, i)):
        file.append(i)
        isdupl.append("dupl5")
        line.append("Empty")
        faction.append("Empty")
        gender.append("Empty")
        #iterator.append(str(len(iterator) + 1))
        print(len(file))

for i in file:
    inlang.append("NO")

data = {'file': file,
        'line': line,
        'faction': faction,
        'gender': gender,
        'isdupl': isdupl,
        'inlang': inlang} 

print( "file: " + str(len(file)) +
      "\nline: " + str(len(line)) + 
      "\nfaction: " + str(len(faction)) + 
      "\ngender: " + str(len(gender)) +
      "\nisdupl: " + str(len(isdupl)))

spreadsheet = pandas.DataFrame(data)
spreadsheet.to_excel('generic_naming.xlsx')