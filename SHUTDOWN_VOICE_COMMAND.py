import os
import pyttsx3
import speech_recognition as sr


class PythonHub:
    def Takecommands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("WAITING FOR YOUR COMMAND")
            self.speak("waiting for your command")
            r.pause_threshold=0.7
            audio=r.listen(source)
            try:
                print("MATCHING")
                self.speak("enforcing your final decision")
                query=r.recognize_google(audio, language='en-in')
                print("THE QUERY IS PRINTED AS='",query,"'")
            except Exception as e:
                print(e)
                print("COMMAND NOT RECOGNIZED PLEASE GIVE ANOTHER ONE")
                return "None"
        return query

    def speak(self, audio):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def quitself(self):
        self.speak("Do you want to terminate all functions and abort this session sir")
        take = self.Takecommands()
        choice = take
        if "yes" in choice:
            print("SHUTTING DOWN THE SYSTEM")
            self.speak("System will be shut down in a moment goodbye")
            self.speak("shutting down the system")
            os.system("shutdown /s /t 30")
        if "no" in choice:
            print("PROCESS ABORTED SUCCESSFULLY")
            self.speak("process aborted because of negative command")
#----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    starter = PythonHub()
    starter.quitself()






