import os 
import shutil

# preparing data from arabic-speech-commands-database

# put all commands in list 

commandsLst = os.listdir("resources/arabic-speech-commands-dataset-master/dataset")
commandsLst.remove('.DS_Store')

# split up data into speaker_n/command_n

for i in range(1, 31):
    
    # for every speaker make a directory

    speakerFolderPath = "tempWav/arSpeechCommands/speaker_" + str(i)
    shutil.rmtree(speakerFolderPath)
    os.mkdir(speakerFolderPath)

    # for every command make a directory
    
    for commandIdx in range(len(commandsLst)):

        commandFolderPath = os.path.join(speakerFolderPath, commandsLst[commandIdx])
        os.mkdir(commandFolderPath)

        datasetCommandPath = os.path.join("resources/arabic-speech-commands-dataset-master/dataset", commandsLst[commandIdx])

        if os.path.isdir(datasetCommandPath):
            for wav in os.listdir(datasetCommandPath):
                if int(wav[0:8]) == i:

                    wavPath = os.path.join(commandFolderPath, wav)
                    datasetWavPath = os.path.join(datasetCommandPath, wav)

                    shutil.copy2(datasetWavPath, wavPath)

# preparing transcriptions and fileid file for speech commands audio files

commandsLstTrans = {'enable' : "تفعيل", 'right' : "يمين", 'eight' : "ثمانية", 'move' : "تحريك", 'cancel' : "إلغاء",
                    'rotate': "تدوير", 'options': "خيارات", 'next': "تالي", 'disable': "تعطيل", 'backward' : "خلف", 
                    'zoom out' : "تصغير", 'close' : "إغلاء", 'record': "تسجيل", 'previous' : "سابق", 'no' : "لا", 
                    'ok' : "وافق", 'nine' : "تسعة", 'left' : "يسار", 'enter': "إدخال", 'start' : "إبدء", 'stop' : "توقف", 
                    'undo' : "ترجع", 'zoom in' : "تكبير", 'three' : "ثلاثة", 'one' : "واحد", 'zero' : "صفر", 'seven' : "سبعة", 
                    'up' : "أعلى", 'two' : "إثنان", 'down' : "أسفل", 'direction' : "اتجاه", 'six' : "ستة", 'yes' : "نعم", 
                    'send' : "إرسال", 'five' : "خمسة", 'open' : "فتح", 'forward' : "أمام", 'digit' : "رقم", 'four' : "أربعة", 
                    "receive" : "إستقبال"}

commTranscriptionFile = open("tempWav/arcommands.transcription", "w")
commFileIDFile = open("tempWav/arcommands.fileids", "w")
n = 1

def sortByUnderscoreNum(lst):
    lstDic = {}
    
    for elem in lst:
        if "_" in elem:
            underScoreIdx = elem.find("_") + 1
            
            if elem[underScoreIdx:].isdigit():
                lstDic[int(elem[underScoreIdx:])] = elem
            
    
    # print(sorted(lstDic.items()))
    # print(dict(sorted(lstDic.items())).values())

    return dict(sorted(lstDic.items())).values()

sortedSpeakerLst = sortByUnderscoreNum(os.listdir("tempWav/arSpeechCommands"))
for speaker in sortedSpeakerLst:

    speakPath = "tempWav/arSpeechCommands/" + speaker

    if os.path.isdir(speakPath):

        for comm in os.listdir(speakPath):
            commandAudioPath = "tempWav/arSpeechCommands/" + speaker + "/" + comm

            if os.path.isdir(commandAudioPath):

                for audio in os.listdir(commandAudioPath):
                    
                    # copy audio files to outer directory and change name to file_n

                    shutil.copy2(commandAudioPath + "/" + audio, speakPath + "/file_" + str(n) + ".wav")

                    # add to transcription file

                    transcriptionStr = "<s> " + commandsLstTrans[comm] + " </s>" + " (file_" + str(n) + ")\n" 
                    commTranscriptionFile.write(transcriptionStr)
                    
                    # add to fileid file
                    
                    fileIDstr = speaker + "/" +  "file_" + str(n) + "\n"
                    commFileIDFile.write(fileIDstr)

                    n = n + 1

commTranscriptionFile.close()
commFileIDFile.close()

# preparing data from MediaSpeech_AR

# for every wav file make a new speaker

mediaSpeechFileLst = os.listdir("resources/MediaSpeech_AR")

# list audio files

mediaSpeechAudioLst = []

for file in mediaSpeechFileLst:
    if file[-4:] == "flac":
        mediaSpeechAudioLst.append(file)

for i in range(31, len(mediaSpeechAudioLst)+1):

    # for every speaker make a directory

    speakerFolderPath = "tempWav/mediaSpeech/speaker_" + str(i)
    shutil.rmtree(speakerFolderPath)
    os.mkdir(speakerFolderPath)

    datasetAudioPath = os.path.join("resources/MediaSpeech_AR/", mediaSpeechAudioLst[i-31])
    audioFilePath = os.path.join(speakerFolderPath, "file_" + str(n) + ".wav")

    shutil.copy2(datasetAudioPath, audioFilePath)

    n = n + 1

