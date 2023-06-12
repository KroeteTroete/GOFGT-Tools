#This file was used to create the sl_naming spreadsheet
import pandas
import os
from os.path import isfile, join

# Spalten:
#     line: transcribed line
#     file: voice line file name
#     faction: which faction voice is used
#     gender: which gender is used

#HORRIBLE SOLUTION
#FOUND BETTER SOLUTION, CAN BE FOUND IN SL_CONV AT LINE 20
#IDK HOW I DIDN'T THINK OF A LOOP, IM TERRIBLY SORRY
slpath = "assets/spaceLounge"
dupl2path = f"{slpath}/dupl2/"
dupl3path = f"{slpath}/dupl3/"
dupl4path = f"{slpath}/dupl4/"
dupl5path = f"{slpath}/dupl5/"
dupl6path = f"{slpath}/dupl6/"
dupl7path = f"{slpath}/dupl7/"
dupl8path = f"{slpath}/dupl8/"
dupl9path = f"{slpath}/dupl9/"
dupl10path = f"{slpath}/dupl10/"
dupl11path = f"{slpath}/dupl11/"
dupl12path = f"{slpath}/dupl12/"
dupl13path = f"{slpath}/dupl13/"
dupl14path = f"{slpath}/dupl14/"
dupl15path = f"{slpath}/dupl15/"
dupl16path = f"{slpath}/dupl16/"
dupl17path = f"{slpath}/dupl17/"
dupl18path = f"{slpath}/dupl18/"
dupl19path = f"{slpath}/dupl19/"
dupl20path = f"{slpath}/dupl20/"
dupl21path = f"{slpath}/dupl21/"
dupl22path = f"{slpath}/dupl22/"
dupl23path = f"{slpath}/dupl23/"
dupl24path = f"{slpath}/dupl24/"
dupl25path = f"{slpath}/dupl25/"
dupl26path = f"{slpath}/dupl26/"
dupl27path = f"{slpath}/dupl27/"
dupl28path = f"{slpath}/dupl28/"
dupl29path = f"{slpath}/dupl29/"
dupl30path = f"{slpath}/dupl30/"
dupl31path = f"{slpath}/dupl31/"
dupl32path = f"{slpath}/dupl32/"
dupl33path = f"{slpath}/dupl33/"
dupl34path = f"{slpath}/dupl34/"
dupl35path = f"{slpath}/dupl35/"
dupl36path = f"{slpath}/dupl36/"
dupl37path = f"{slpath}/dupl37/"
dupl38path = f"{slpath}/dupl38/"
dupl39path = f"{slpath}/dupl39/"
dupl40path = f"{slpath}/dupl40/"
dupl41path = f"{slpath}/dupl41/"
dupl42path = f"{slpath}/dupl42/"
dupl43path = f"{slpath}/dupl43/"
dupl44path = f"{slpath}/dupl44/"
dupl45path = f"{slpath}/dupl45/"
dupl46path = f"{slpath}/dupl46/"

dirs = [
    dupl2path,
    dupl3path,
    dupl4path,
    dupl5path,
    dupl6path,
    dupl7path,
    dupl8path,
    dupl9path,
    dupl10path,
    dupl11path,
    dupl12path,
    dupl13path,
    dupl14path,
    dupl15path,
    dupl16path,
    dupl17path,
    dupl18path,
    dupl19path,
    dupl20path,
    dupl21path,
    dupl22path,
    dupl23path,
    dupl24path,
    dupl25path,
    dupl26path,
    dupl27path,
    dupl28path,
    dupl29path,
    dupl30path,
    dupl31path,
    dupl32path,
    dupl33path,
    dupl34path,
    dupl35path,
    dupl36path,
    dupl37path,
    dupl38path,
    dupl39path,
    dupl40path,
    dupl41path,
    dupl42path,
    dupl43path,
    dupl44path,
    dupl45path,
    dupl46path
]

line = []
file = []
faction = []
gender = []
isdupl = []

#iterator = []

spalten = [line,file,faction,gender,isdupl]

# for i in range(0, 130):
#     iterator.append(str(i))

for i in os.listdir(slpath):
    if isfile(join(slpath, i)):
        file.append(i)
        # print(len(file))

for i in file:
    line.append("EMPTY")
    isdupl.append("None")
    faction.append("EMPTY")
    gender.append("EMPTY")

#dupl loops
duplcounter = 1
for i in dirs:
    duplcounter += 1
    for j in os.listdir(i):
        if isfile(join(i, j)):
            file.append(j)
            if duplcounter != 1:
                isdupl.append("dupl" + str(duplcounter))
            line.append("Empty")
            faction.append("Empty")
            gender.append("Empty")
            #iterator.append(str(len(iterator) + 1))
            print(len(file))
    

data = {'file': file,
        'line': line,
        'faction': faction,
        'gender': gender,
        'isdupl': isdupl} 

print( "file: " + str(len(file)) +
      "\nline: " + str(len(line)) + 
      "\nfaction: " + str(len(faction)) + 
      "\ngender: " + str(len(gender)) +
      "\nisdupl: " + str(len(isdupl)))

spreadsheet = pandas.DataFrame(data)
spreadsheet.to_excel('sl_naming.xlsx')