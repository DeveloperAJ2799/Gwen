import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import google.generativeai as genai


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine .setProperty('voice', voices[1].id )

genai.configure(api_key="add your api key")


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Moring") 
    elif hour>= 12 and hour<18:
        speak("Good Afternoon") 
    else:
         speak("Good Evening")  

    speak("I am gwen and how may i help you")   
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .5
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
            
        print("Say that again please...") 
        return "None" 
    return query                   


    

if __name__== "__main__":
    wishMe()
    while True:
        query = takecommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            googleopen = "C:\Program Files\Google\Chrome\Application\chrome.exe" 
            os.startfile(googleopen)

        
        
        elif 'open Opera GX' in query:
            gxbrowser = "C:\\Users\\ayaan\\AppData\\Local\\Programs\\Opera GX\launcher.exe"
            os.startfile(gxbrowser)
        else:
            generation_config = {
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }

            model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            )

            chat_session = model.start_chat(
            history=[
             ]
            )
  
            response = chat_session.send_message(query)
            print(response.text)
            speak(response.text)
            

