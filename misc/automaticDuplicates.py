# This script automatically creates the dupl folders for sound files that have been extracted from a .fsb using Aezay's FSBExtractor
import os
from os.path import isfile, join, exists
import shutil


def extractBrackets(string):

    bracketContent = ""
    lst = []

    if "(" in string:
        for letter in string:
            lst.append(letter)
        openingBracket = lst.index("(")
        closingBracket = lst.index(')')
    
    for i in range(openingBracket + 1, closingBracket):
        bracketContent = bracketContent + str(lst[i])
    #print(lst)
    #print(str(openingBracket) + " to " + str(closingBracket) + ". Content:" + bracketContent + "END")

    return(bracketContent)

assetFolder = "assets\\spaceLounge\\"

for i in os.listdir(assetFolder):
    
    if "(" in i:
        bracket = extractBrackets(i)
        duplFolderName = "dupl" + bracket
        print(duplFolderName)

        if not os.path.exists(assetFolder + duplFolderName):
            os.makedirs(assetFolder + duplFolderName)
            shutil.move(assetFolder + i, assetFolder + duplFolderName + "\\" + i)
            name = assetFolder + duplFolderName + "\\" + i
            newname = name.replace(f" ({bracket})", "")
            os.rename(assetFolder + duplFolderName + "\\" + i, newname)
        else:
            print(duplFolderName + " already exists")
            shutil.move(assetFolder + i, assetFolder + duplFolderName + "\\" + i)
            name = assetFolder + duplFolderName + "\\" + i
            newname = name.replace(f" ({bracket})", "")
            os.rename(assetFolder + duplFolderName + "\\" + i, newname)


