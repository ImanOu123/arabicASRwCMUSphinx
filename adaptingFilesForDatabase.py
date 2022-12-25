import os 
import shutil
import dataPrepForDatabase

# combine audio files in 'tempWav/wav' directory

for dir in dataPrepForDatabase.sortByUnderscoreNum(os.listdir("tempWav/arSpeechCommands")):

    dirPath = os.path.join("tempWav/arSpeechCommands",dir)
    if os.path.isdir(dirPath):
        newSpeakDirPath = "tempWav/wav/" + dir

        shutil.rmtree(newSpeakDirPath)
        os.mkdir(newSpeakDirPath)

        for file in dataPrepForDatabase.sortByUnderscoreNum(os.listdir(dirPath)):      
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath) and "wav" in file:
                speakDirPath = "tempWav/arSpeechCommands/" + dir

                shutil.copy2(os.path.join(speakDirPath, file), os.path.join(newSpeakDirPath, file))

for dir in dataPrepForDatabase.sortByUnderscoreNum(os.listdir("tempWav/mediaSpeech")):

    dirPath = os.path.join("tempWav/mediaSpeech",dir)
    if os.path.isdir(dirPath):
        newSpeakDirPath = "tempWav/wav/" + dir

        shutil.rmtree(newSpeakDirPath)
        os.mkdir(newSpeakDirPath)
        
        for file in dataPrepForDatabase.sortByUnderscoreNum(os.listdir(dirPath)):            
            filePath = os.path.join(dirPath, file)
            if os.path.isfile(filePath) and "wav" in file:
                speakDirPath = "tempWav/mediaSpeech/" + dir

                shutil.copy2(os.path.join(speakDirPath, file), os.path.join(newSpeakDirPath, file))


# copying relevant audio files to the main database directory

shutil.rmtree("arabicASRDatabase/wav")
shutil.copytree("tempWav/wav", "arabicASRDatabase/wav")

# shutil.copy2("tempWav/arabicASRDatabase_train.fileids", "arabicASRDatabase/etc/arabicASRDatabase_train.fileids")
# shutil.copy2("tempWav/arabicASRDatabase_test.fileids", "arabicASRDatabase/etc/arabicASRDatabase_test.fileids")

# shutil.copy2("tempWav/arabicASRDatabase_train.transcription", "arabicASRDatabase/etc/arabicASRDatabase_train.transcription")
# shutil.copy2("tempWav/arabicASRDatabase_test.transcription", "arabicASRDatabase/etc/arabicASRDatabase_test.transcription")