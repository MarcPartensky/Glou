import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

def record():
    with mic as source:
        audio = r.listen(source)
    return r.recognize_google(audio, language='fr-FR')
