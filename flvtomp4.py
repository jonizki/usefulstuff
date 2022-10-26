import subprocess
import os

# Source folder where .flv filenames are located
src = os.getcwd()
# Destination wheere .mp4 filenames are saved
dst = os.getcwd()

for root, dirs, filenames in os.walk(src, topdown=False):
    for filename in filenames:
        if ".flv" in filename:
            inputfile = os.path.join(root, filename)
            outputfile = os.path.join(dst, filename.replace(".flv", ".mp4"))
            subprocess.run(['ffmpeg', '-i', inputfile, outputfile])  
