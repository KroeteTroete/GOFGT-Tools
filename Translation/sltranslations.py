# This was used to translate the content of the space lounge .fsb
import pandas as pd
import gof2translate as gt

langData = pd.read_excel("comparison.xlsx")
langDF = pd.DataFrame(langData, columns=["vanilla", "modded"])

genericData = pd.read_excel("sl_naming.xlsx")
genericDF = pd.DataFrame(genericData, columns=["line", "faction", "gender", "file", "isdupl"])

genericLines = genericDF["line"].to_list()
genericFactions = genericDF["faction"].to_list()
genericGenders = genericDF["gender"].to_list()
genericFiles = genericDF["file"].to_list()
genericDuplChecks = genericDF["isdupl"].to_list()

langVanilla = langDF["vanilla"].to_list()
langModded = langDF["modded"].to_list()

translationPool = {}

translatedLines = []

iterator = -1
for i in genericLines:

    iterator += 1

    if i in translationPool.keys():

        print("Line in translationpool")
        translatedLines.append(translationPool.get(i))
    
    else:
        #if not already translated, translate it
        transl = gt.breaktranslation(i)

        translatedLines.append(transl)

        print("Line added to translation pool")
        translationPool[i] = transl

newData = {'file': genericFiles,
        'line': translatedLines,
        'faction': genericFactions,
        'gender': genericGenders,
        'isdupl': genericDuplChecks}

print( "file: " + str(len(genericFiles)) +
      "\nline: " + str(len(translatedLines)) + 
      "\nfaction: " + str(len(genericFactions)) + 
      "\ngender: " + str(len(genericGenders)) +
      "\nisdupl: " + str(len(genericDuplChecks)))

spreadsheet = pd.DataFrame(newData)
spreadsheet.to_excel("sl_translated.xlsx")
