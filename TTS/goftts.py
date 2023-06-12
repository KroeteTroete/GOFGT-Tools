# This script was used to create the tts files for the standard .fsb file and .lang file
import pandas as pd
import festipy as fp
import os

tableData = pd.read_excel("comparison.xlsx")
df = pd.DataFrame(tableData, columns=['speaker', 'vanilla', 'modded'])

vanilla = tableData['vanilla'].tolist()
modded = tableData['modded'].tolist()
speaker = tableData['speaker'].tolist()

lowerBoundary = 2044 #Inclusive
upperBoundary = 2046 #Exclusive



voices = [
    "cmu_us_slt_arctic_clunits",
    "cmu_us_clb_arctic_clunits",
    "cmu_us_jmk_arctic_clunits",
    "cmu_us_bdl_arctic_clunits",
    "cmu_us_awb_arctic_clunits",
    "cmu_us_ksp_arctic_clunits",
    "cmu_us_rms_arctic_clunits",
    "us1_mbrola",
    "us3_mbrola"
    ]

festival = fp.festipy()

for i in range(lowerBoundary, upperBoundary):
            
    festival.startFestival()
    
    voiceID = int(speaker[i])

    if voiceID == 0:

        continue
    
    
    wavname = f'TTS_{i}_{voiceID}.wav'

    if os.path.exists(wavname):

        print(f"{wavname} already exists")
        festival.spTerminate()
        continue
    
    while not os.path.exists(wavname):
        
        festival.setVoice(voices[voiceID - 1])

        if i == 2044 or i == 2045:
            
            sep = ". "

            multiLine = sep.join(modded[i].replace('"', "'").split("\n"))

            print(multiLine)

            festival.ttsFile(multiLine, wavname)

        else:

            festival.ttsFile(modded[i], wavname)

        festival.spTerminate()
        
festival.spTerminate()