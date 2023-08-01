import pyttsx3
tts=pyttsx3.init()
voices=tts.getProperty('voices')
for voice in voices:
    print('=====','Name: %s'%voice.name,'ID: %s'%voice.id,'Lang: %s'%voice.languages,'Gender: %s'%voice.gender,'Age: %s'%voice.age,sep='\n')
