# combine all text to one file
import os
import subprocess
from pathlib import Path
import maha
from maha.processors import StreamFileProcessor
from maha.cleaners.functions import numbers_to_text
from maha.cleaners.functions import remove

# os.remove("train-text1.txt")

# wf = open("train-text.txt", "w")

# dirNameLst = ["akhbarona/Test", "akhbarona/Train"]

# # iterate of files in directory
# for dirName in dirNameLst:
#     for dir in os.listdir(dirName):
#         fName = os.path.join(dirName, dir)
#         if os.path.isdir(fName):
#             subDir = os.listdir(fName)
#             for filename in subDir:
#                 txtFile = os.path.join(fName, filename)

#                 # extract lines from file 
#                 with open(txtFile) as f:
#                     lines = f.readlines()
                
#                 if "// <![CDATA[\n" in lines:
#                     lines = lines[:lines.index("// <![CDATA[\n")]

#                 linesStr = "".join(lines).replace("Title\n", "").replace("Body\n", "")
                    
#                 wf.write(linesStr)

# wf.close()

# clean text in main training data file

# resource_path = "train-text.txt"

# proc = StreamFileProcessor(resource_path)
# proc = proc.normalize(all=True).drop_empty_lines().keep(arabic_letters=True, punctuations=True, english_numbers=True, arabic_numbers=True)

# # To start processing the file, run the following commented code.

# proc.process_and_save(Path("train-text1.txt"))


with open("train-text1.txt") as f:
    forProcessLinesLst = f.readlines()

mainDataFile = open("train-text2.txt", "w")

# change numbers to text

longNums = "65959596 99165456 23734447 23734446 22444117 97600074 22444117 97600074 22444117 97600074 1984198619881991199620012003200520082012 19581968197019922014 2004200820122016 1958  1962  1970  1994  2002 1934  1938  1982  2006 1954  1974  1990  2014"

for idx in range(len(forProcessLinesLst)):
    line = forProcessLinesLst[idx]
    line = line.replace("-", "").replace("%", "")
    
    # replacing long numbers

    for num in longNums.split(" "):
        line = line.replace(num, "")

    # converting rest of the numbers to text

    try:
        forProcessLinesLst[idx] = numbers_to_text(line)
    except ValueError:
        forProcessLinesLst[idx] = line

    # split sentences on lines

    forProcessLinesLst[idx] = forProcessLinesLst[idx].replace(".", "\n")
    forProcessLinesLst[idx] = forProcessLinesLst[idx].replace("(", "\n")
    forProcessLinesLst[idx] = forProcessLinesLst[idx].replace(")", "\n")

    # remove punctuation

    forProcessLinesLst[idx] = remove(forProcessLinesLst[idx], punctuations=True)

forProcessLines = "".join(forProcessLinesLst)

mainDataFile.write(forProcessLines)

mainDataFile.close()