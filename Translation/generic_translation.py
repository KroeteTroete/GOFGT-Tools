# This script was used to "translate" the generic .fsb content
# gof2translate (a branch of random-googletrans, which can be found on my GitHub is needed for this)
import pandas as pd
import gof2translate as gt

langData = pd.read_excel("comparison.xlsx")
langDF = pd.DataFrame(langData, columns=["vanilla", "modded"])

genericData = pd.read_excel("generic_naming.xlsx")
genericDF = pd.DataFrame(genericData, columns=["line", "inlang", "faction", "gender", "file", "isdupl"])

genericLines = genericDF["line"].to_list()
genericLangChecks = genericDF["inlang"].to_list()
genericFactions = genericDF["faction"].to_list()
genericGenders = genericDF["gender"].to_list()
genericFiles = genericDF["file"].to_list()
genericDuplChecks = genericDF["isdupl"].to_list()

langVanilla = langDF["vanilla"].to_list()
langModded = langDF["modded"].to_list()


translatedLines = []

iterator = -1
for i in genericLines:

    iterator += 1

    if genericLangChecks[genericLines.index(i)] != "NO":

        print(f"Line {iterator} has the lang equivalent {genericLangChecks[genericLines.index(i)]}")

        #look for index in already translated modded langs and add that to the list for the new spreadsheet
        translatedLines.append(langModded[int(genericLangChecks[genericLines.index(i)])])

    elif genericLangChecks[genericLines.index(i)] == "NO":

        #if not alreaddy translated, translate it
        transl = gt.breaktranslation(i)

        translatedLines.append(transl)

newData = {'file': genericFiles,
        'line': translatedLines,
        'faction': genericFactions,
        'gender': genericGenders,
        'isdupl': genericDuplChecks,
        'inlang': genericLangChecks}

print( "file: " + str(len(genericFiles)) +
      "\nline: " + str(len(translatedLines)) + 
      "\nfaction: " + str(len(genericFactions)) + 
      "\ngender: " + str(len(genericGenders)) +
      "\nisdupl: " + str(len(genericDuplChecks)) +
      "\ninLang: " + str(len(genericLangChecks)))

spreadsheet = pd.DataFrame(newData)
spreadsheet.to_excel("generic_translated.xlsx")
