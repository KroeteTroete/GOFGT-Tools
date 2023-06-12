# Pandas as well as langdetect (which can be found on my GitHub) are needed for this
# This was used to create a spreadsheet to compare and edit attributes of .lang files
import pandas as pd
import langdetect as ld

vanilla = ld.extractLang("gb.lang")
modded = ld.extractLang("modded.lang")
langtype=[]
# types:
#     std = standard
#     mis = space lounge mission (may derive from spoken text)
#     pir = pirate station notifs (may derive from spoken text)
#     dlg = dialogue (always the same as spoken text)
#     car = carla paolini annoying the player about sahi
#     fff = translation failure
speaker=[]
mistakes=[]
audio = []

for i in range(len(vanilla)):
    langtype.append("std")

for i in range(len(vanilla)):
    speaker.append(0)

for i in range(len(vanilla)):
    mistakes.append("No mistake")

for i in range(len(vanilla)):
    audio.append("Empty")

if len(vanilla) != len(modded):
    print("length is not equal")

else:
    print("length is equal")

print(len(vanilla))
indexes = range(len(vanilla))
print(len(modded))
print(len(indexes))
print(len(speaker))
print(len(mistakes))

data = {'type': langtype,
        'speaker': speaker,
        'equal': mistakes,
        'vanilla': vanilla,
        'modded': modded
        }

answer = input("What action do you want to perform?\n1. Compare .langs\n2. Write Spreadsheet")

if answer == "2":

    errors = 0
    errorExport = "### Exported errors of the last comparelang execution ###"

    for i in vanilla:

        if vanilla[vanilla.index(i)] == modded[vanilla.index(i)]:
            errorExport = errorExport + "\nPossible failed seperation at index " + str(vanilla.index(i))

            mistakes[vanilla.index(i)] = "Possible Mistake"
            errors += 1
        
        else:
            continue

    print(str(errors) + " possible mistakes found")
    spreadsheet = pd.DataFrame(data)

    spreadsheet.to_excel('comparison.xlsx')

    with open("langcompare_ERRORS.txt", 'w') as f:
        f.write(errorExport)

        f.close()

elif answer == "1":

    for i in vanilla:

        errors = 0

        if vanilla[vanilla.index(i)] == modded[vanilla.index(i)]:
            print("Possible failed seperation at index " + str(vanilla.index(i)))
            errors += 1
        
        else:
            continue
    
    print(str(errors) + " possible mistakes found")



