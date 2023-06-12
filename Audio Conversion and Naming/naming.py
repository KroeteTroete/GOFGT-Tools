# This script was used to convert the .lang file comparison table to TTS
# requires pandas
import pandas
import os
import shutil
import time

Rsubfolder = "REMINDERS"
subfolder = "Reminders"

lower = 513 #Inclusive
upper = 518 #Exclusive

RENAMED = f"ttswavs/RENAMED/{Rsubfolder}/"
UNNAMED = f"ttswavs/{subfolder}/"
print(os.listdir(RENAMED))

tableData = pandas.read_excel("comparison.xlsx")
df = pandas.DataFrame(tableData, columns=['speaker', 'audio'])

audio = tableData['audio'].tolist()
speaker = tableData['speaker'].tolist()

IDrange = range(lower, upper)

for i in IDrange:

    wavname = f'TTS_{i}_{speaker[i]}.wav'
    print(wavname)

    if audio[i] != "Empty":

        if int(speaker[i]) == 0:
            print(f"\n\n\n NO SPEAKER AT ITEM {i} \n\n\n")

            with open("missing_speakers.txt", "w") as f:
                f.write(f"NO SPEAKER AT ITEM {i}\n")
                f.close()

            time.sleep(1)
            continue

        shutil.copy2(UNNAMED + wavname, RENAMED)
        os.rename(RENAMED + wavname, RENAMED + f"{audio[i]}.wav")
        
        wav1 = f"insert path here\\{Rsubfolder}\\""

        wav2 = f"{audio[i]}.wav"
        print(wav1+wav2)
        command = "ffmpeg -i "+wav1+wav2+" -vn -ar 44100 -ac 2 -b:a 192k -filter:a \"volume=9dB\" "+wav1+"mp3\\"+audio[i]+".mp3"
        os.system(command)
        
