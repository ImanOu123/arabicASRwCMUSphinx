# combine all text to one file
import os

# os.remove("train-text1.txt")

wf = open("train-text.txt", "w")

dirNameLst = ["akhbarona/Test", "akhbarona/Train"]

# iterate of files in directory
for dirName in dirNameLst:
    for dir in os.listdir(dirName):
        fName = os.path.join(dirName, dir)
        if os.path.isdir(fName):
            subDir = os.listdir(fName)
            for filename in subDir:
                txtFile = os.path.join(fName, filename)

                # extract lines from file 
                with open(txtFile) as f:
                    lines = f.readlines()
                
                if "// <![CDATA[\n" in lines:
                    lines = lines[:lines.index("// <![CDATA[\n")]

                linesStr = "".join(lines).replace("Title\n", "").replace("Body\n", "")
                    
                wf.write(linesStr)

wf.close()

# clean text in main training data file

from pathlib import Path
import maha
from maha.processors import StreamFileProcessor
from maha.cleaners.functions import numbers_to_text

resource_path = "train-text.txt"

proc = StreamFileProcessor(resource_path)
proc = proc.normalize(all=True).drop_empty_lines().keep(arabic_letters=True, punctuations=True, english_numbers=True, arabic_numbers=True)

# To start processing the file, run the following commented code.

proc.process_and_save(Path("train-text1.txt"))

with open("train-text1.txt") as f:
    forProcessLinesLst = f.readlines()

forProcessLines = "".join(forProcessLinesLst)

# remove '-' 
forProcessLines = forProcessLines.replace("-", "0")

mainDataFile = open("train-text2.txt", "w")

# change numbers to text

postProcessLines = numbers_to_text(forProcessLines)
mainDataFile.write(postProcessLines)

# split sentences on lines
# for i in

# remove punctuation

mainDataFile.close()