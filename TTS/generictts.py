# This script was used to create the tts files for the "generic" .fsb file
import pandas as pd
import festipy as fp
import os

tableData = pd.read_excel("generic_translated.xlsx")
df = pd.DataFrame(tableData, columns=["file", "line", "faction", "gender", "isdupl"])

files = df["file"].to_list()
lines = df["line"].to_list()
factions = df["faction"].to_list()
genders = df["gender"].to_list()
duplChecks = df["isdupl"].to_list()


voices = [
    "cmu_us_ksp_arctic_clunits",
    "cmu_us_bdl_arctic_clunits",
    "cmu_us_rms_arctic_clunits",
    "cmu_us_jmk_arctic_clunits",
    "cmu_us_slt_arctic_clunits",
    "cmu_us_awb_arctic_clunits",
    "cmu_us_bdl_arctic_clunits"
]

festival = fp.festipy()

iterator = -1

for i in lines:

    voice = ""

    iterator += 1
    
    assignedFaction = factions[iterator]
    assignedGender = genders[iterator]

    festival.startFestival()

    print(f"Line {iterator} has faction {assignedFaction}")

    if assignedFaction == 1:
        voice = "cmu_us_ksp_arctic_clunits"
        print(f"assigned voice {voice}")

    elif assignedFaction == 2:
        voice = "cmu_us_bdl_arctic_clunits"
        print(f"assigned voice {voice}")

    elif assignedFaction == 3:
        voice = "cmu_us_rms_arctic_clunits"
        print(f"assigned voice {voice}")

    elif assignedFaction == 4 and assignedGender == "EMPTY" or "Empty":
        voice = "cmu_us_jmk_arctic_clunits"
        print(f"assigned voice {voice}")

    elif assignedFaction == 4 and assignedGender == "f":
        voice = "cmu_us_slt_arctic_clunits"
        print(f"assigned voice {voice}")

    elif assignedFaction == 5:
        voice = "cmu_us_awb_arctic_clunits"
        print(f"assigned voice {voice}")

    elif assignedFaction == 6:
        voice = "cmu_us_bdl_arctic_clunits"
        print(f"assigned voice {voice}")

    else:
        print(f"Something went wrong at iterator {iterator}") 
        break

    wavname = files[iterator].replace(".mp3", ".wav")
    completepath = ""
    duplFolder = ""

    if duplChecks[iterator] != "None":

        if duplChecks[iterator] == "dupl1":
            duplFolder = "/dupl/"
        
        else:
            duplFolder = f"/{duplChecks[iterator]}/"

        completepath = f"ttsgeneric/{duplFolder}/{wavname}"
    
    else:
        completepath = f"ttsgeneric/{wavname}"

    festival.setVoice(voice)
    festival.ttsFile(i, completepath)
    festival.spTerminate()
