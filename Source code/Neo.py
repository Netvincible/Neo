
import pyttsx3
import datetime
import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate   = engine.getProperty('rate')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=12 and hour<16:
        speak("Good Afternoon Sir")
    elif hour<12:
        speak("Good Morning Sir")
    else:
        speak("Good Evening Sir")
    
    #playsound.playsound('D:\\Projects\\Python\\Jarvis\\Media\\Audio\\Jarvis Introduction.mp3')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Please tell how may I assist you sir")
        r.pause_threshold=0.8
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio, language='en-in')
        print("You said: ", query)

    except Exception as e:
        print("Error: Please try checking your Internet Connection")
        speak("Error")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            query=query.replace("wikipedia", "")
            speak("Searching Wikipedia")
            print(f"Searching for: {query}")
            results=wikipedia.summary(query, sentences=2)
            print("According to wikipedia: ", results)
            speak(f"According to Wikipedia{results}")

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir the time is: {strtime}")
            print(f"Sir the time is {strtime}")

        elif 'search for' in query:
            query=query.replace("search for", "")
            webbrowser.open(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="D:\\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open code' in query:
            codepath="D:\\Tools\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'open spotify' in query:
            spotifypath=""
            os.startfile(spotifypath)
            
        elif 'open whatsapp' in query:
            whatsapppath="C:\\Users\\sorat\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapppath)

        elif 'open browser' in query:
            browserpath="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(browserpath)

        elif 'call your mom' in query:
            cortanapath="C:\Program Files\WindowsApps\Microsoft.549981C3F5F10_3.2109.6305.0_x64__8wekyb3d8bbwe\Cortana.exe"
            os.startfile(cortanapath)

        elif 'call your dad' in query:
            linkpath="C:\\Users\\sorat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Mega-Voice-Command\\LINKS\\LINKS - Mark II.appref-ms"
            os.startfile(linkpath)
        
        elif 'fire up desktop' in query:
            rockpath="D:\\Tools\\RocketDock\\RocketDock.exe"
            os.startfile(rockpath)
            rainpath="D:\\Rainmeter\\Rainmeter.exe"
            os.startfile(rainpath)