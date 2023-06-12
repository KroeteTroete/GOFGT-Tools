# This script was used to convert the tts sound files from the "generic" fsb to mp3, as well as increase their volume
import os
import time
from os.path import isfile, join

wavPath = "ttsgeneric\\"
wavDuplePath1 = "ttsgeneric\\dupl\\"
wavDuplePath2 = "ttsgeneric\\dupl2\\"
wavDuplePath3 = "ttsgeneric\\dupl3\\"
wavDuplePath4 = "ttsgeneric\\dupl4\\"
wavDuplePath5 = "ttsgeneric\\dupl5\\"

def convertFilesInFolder(folderPath):

    for i in os.listdir(folderPath):
        if isfile(join(folderPath, i)):
            fileWithoutExtension = i.replace(".wav", "")
            command = "ffmpeg -i "+folderPath+i+" -vn -ar 44100 -ac 2 -b:a 192k -filter:a \"volume=9dB\" "+folderPath+"mp3\\"+fileWithoutExtension+".mp3"
            os.system(command)
            time.sleep(1)
        else:
            print(i + " is not a file")

convertFilesInFolder(wavDuplePath5)