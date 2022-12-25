from maha.cleaners.functions import contains
import pyarabic.trans

# creating a dictionary from scratch

# extract words from dictionary corpus

dicCorpusFile = open("dict-corpusSMALL.txt", 'r')

dicCorpusWords = dicCorpusFile.read().split(" ")

# create new dictionary file with word and transliteration

dictFile = open("nonCMUDiSMALL.dic", 'w')

dicCorpusWords = list(set(dicCorpusWords))

for word in dicCorpusWords:
    if contains(word, arabic=True):
        strToWr = word + "      " + " ".join(pyarabic.trans.convert(word,'arabic','tim')) + "\n"
        dictFile.write(strToWr)

dictFile.close()