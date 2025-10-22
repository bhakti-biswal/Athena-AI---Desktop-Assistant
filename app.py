import speech_recognition as sr
import webbrowser
import pyttsx3
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()



#speek        
def speek(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

#________________________________________________________________________________________________________________#
# Open apps
def open_app(app_name):
    if app_name == "chrome":
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif app_name == "notepad":
        os.system("notepad")
    elif app_name == "vscode":
        os.startfile("C:\\Users\\YourUser\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

# Close apps
def close_app(app_name):
    if app_name == "chrome":
        os.system("taskkill /f /im chrome.exe")
    elif app_name == "notepad":
        os.system("taskkill /f /im notepad.exe")
    elif app_name == "vscode":
        os.system("taskkill /f /im Code.exe")   ####

def process_command(command):
    command=command.lower()
    if "open google" in command:
        speek("Opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speek("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in command:
        speek("Opening chatgpt")
        webbrowser.open("https://chatgpt.com")
    elif "open facebook" in command:
        speek("Opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open flipkart" in command:
        speek("Opening flipkart")
        webbrowser.open("https://flipkart.com")
    elif "open amazon" in command:
        speek("Opening amazon")
        webbrowser.open("https://amazon.com")
    elif "open x" in command:
        speek("Opening x")
        webbrowser.open("https://x.com")
    elif "open chrome" in command:
        speek("Opening chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "open notepad" in command:
        speek("Opening notepad")
        os.system("notepad")
    elif "open vscode" in command:
        speek("Opening vscode")
        os.startfile("C:\\Users\\bhakt\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif "open whatsapp" in command:
        speek("Opening Whatsapp")
        os.startfile("C:\\Users\\bhakt\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    

#___________________________________________________________________________________________________________________________________#


if __name__=="__main__":
    print("Loading")
while True:
    r = sr.Recognizer()
    # recognize speech using google   
    try:
        with sr.Microphone() as source:
            print("Listening..")
            audio = r.listen(source)
        cmd=r.recognize_google(audio).lower()
        #print(cmd)
        # Response to User  ### Wake Word
        if "athena" in cmd:
            speek("Yes Sir")
            print("Activate")
            # Listen For Command 
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source)
                command=r.recognize_google(audio)

                process_command(command)

    except sr.UnknownValueError:
                ("Didn't catch that. Waiting again...")
    except sr.RequestError as e:
                speek("API unavailable:", e)
