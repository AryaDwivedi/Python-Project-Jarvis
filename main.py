import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    genai.configure(api_key="")

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(command)
    return(response.text)
    
def processcCommand(c):   
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open geeks" in c.lower():
        webbrowser.open("https://www.geeksforgeeks.org/")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] # let play chand first it will do lower then split will convert it into a list ["play" , "chand"] then we will chose [1] of the list i.e chand or any other song
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    else:
        # Let Gemini handle the request
        output  = aiProcess(c)
        speak(output)
    
if __name__ =="__main__":
    speak("Iniitializing Jarvis....")
    
    while True:
        # Listen for the wake word Jarvis
        r = sr.Recognizer()
        
        print("recognizing")
        

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source ,timeout = 2 , phrase_time_limit=1)
            word = r.recognize_google(audio)
          
          
            if(word.lower() == "jarvis"):
                speak("I am On")
                # Listen for command
                
                with sr.Microphone() as source:
                    print("Jarvis Activated!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    
                    processcCommand(command)
                    
      
        except Exception as e:
            print("error; {0}".format(e))
        
    
    
