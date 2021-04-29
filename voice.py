# recognizer_instance.recognize_google(language = "pl-PL")
import speech_recognition as sr
import keyboard
import threading
import commandHandler
import discordMusic



def run():
    detector = sr.Recognizer()
    while True:
        while True:
            with sr.Microphone() as source:
                print("Speak Anything :")
                audio = detector.listen(source, timeout=1500,)
                print("after record")
                try:
                    text = detector.recognize_google(audio, language="pl-PL")
                    print("You said : {}".format(text))
                    x = threading.Thread(target=commandHandler.handleCommand, args=(text,))
                    x.start()
                    # self.f.write("\n")
                    # self.f.write(text)
                except:
                    print("nic")


#print(sr.Microphone.list_microphone_names())
# y = threading.Thread(target=discordMusic.runBot(), args=())
# y.start()
run()
