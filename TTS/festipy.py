#This is a simple and minimalistic festival wrapper

import subprocess as sp
import time
import os

# cmu_us_slt_arctic_clunits
# cmu_us_clb_arctic_clunits
# cmu_us_jmk_arctic_clunits
# cmu_us_bdl_arctic_clunits
# cmu_us_awb_arctic_clunits
# cmu_us_ksp_arctic_clunits
# cmu_us_rms_arctic_clunits


class festipy():


    def __init__(self, args: list = []):
        
        self.args = args

        global festival_process
    
    def startFestival(self):

        global festival_process

        festival_process = sp.Popen("festival", stdin=sp.PIPE, stdout=sp.PIPE)
        print("started festival process")

    def setVoice(self, voice: str):


        festival_process.stdin.write(f'(voice_{voice})\n'.encode())
        festival_process.stdin.flush()

        activeVoice = voice
        print(f"voice {voice}")

    def sayText(self, text):
        
        festival_process.stdin.write(f'(SayText "{text}")\n'.encode())
        festival_process.stdin.flush()

        output = festival_process.stdout.readline()
        print(output.decode())

    def ttsFile(self, text, filename):
            
            # create the script for festival
            script = f'(utt.save.wave (SayText "{text}") "{filename}" "riff")'
            
            # send the script to festival
            festival_process.stdin.write(script.encode())
            festival_process.stdin.flush()
            
            # wait for the file to be created
            while not os.path.exists(filename):
                time.sleep(0.1)
            
            print(f"file saved as {filename}")

    def spTerminate(self):

        festival_process.stdin.write(f'(exit)\n'.encode())
        festival_process.stdin.flush()
        festival_process.terminate()
        print("Process terminated")

