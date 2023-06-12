# This script was used to convert the space lounge tts files

import os
import time
from os.path import isfile, join

wavPath = "ttslounge\\"

def convertFilesInFolder(folderPath):

    for i in os.listdir(folderPath):
        if isfile(join(folderPath, i)):
            fileWithoutExtension = i.replace(".wav", "")
            command = "ffmpeg -i "+folderPath+i+" -vn -ar 44100 -ac 2 -b:a 192k -filter:a \"volume=9dB\" "+folderPath+"mp3\\"+fileWithoutExtension+".mp3"
            os.system(command)
            time.sleep(1)
        else:
            print(i + " is not a file")

# for i in range(2, 47):
#     time.sleep(1)
#     print("Starting in dupl folder "+str(i))
#     convertFilesInFolder(wavPath + "dupl" + str(i) + "\\")

convertFilesInFolder(wavPath + "dupl11\\")