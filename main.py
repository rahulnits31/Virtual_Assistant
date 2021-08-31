
#import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import speech_recognition as sr
import wikipedia 
import pyttsx3
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)  # voices[0] or voices[1].id are two different voices of windows one being a male and the other a female




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
        
    speak("I am Veronica sir, your personal Virtual Assistant. Please tell me how may i assist you.")        



def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
        try:
            print("Recognizing....")
            query=r.recognize_google(audio, language='en-in')
            #print("user said:",query)
            #using fstring
            print(f"User said :{query}\n")
        except Exception as e:
            #print(e)       # Comment it to hide the exception
            print("Say that again please....")
            return "None"
        return query
        
    
        
     
        def sendMail(to, content):
            server= smtplib.SMTP('smtp.gmail.com', 587) # create a mail server on port 587
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('yourmailid@gmail.com', 'passwword')
            server.sendmail('receivermailid@gmail.com', to, content)
            server.close()
            
            
       
            
            
 









if __name__ == "__main__":
    speak("Hello there!")
    print("Hello there!")
    wishme()

while True:
    query=takeCommand().lower()
    
    
    if 'quit' in query:
        break
    
   
    
    
    # logic for execution of task based on query
    
    if 'wikipedia' in query:
        speak("Searching Wikipedia....")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open geeksforgeeks' in query:
        webbrowser.open("geeksforgeeks.org")
    
    
    
    
    
    
    

    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open hindu' in query:
        webbrowser.open("thehindu.com")
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open rotten'in query:
        webbrowser.open("rottentomatoes.com")

    elif 'open medium'in query:
        webbrowser.open("medium.com")

    elif 'open imdb' in query:
        webbrowser.open("imdb.com")

    elif 'music' in query:
        music_dir='C:\\Users\\RAHUL DEB\\Music\\Vintage songs'         # add directory path as per the use-case
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    
    elif 'open fifa' in query:
        fifapath="C:\\Program Files\\FIFA18\\FIFA18.exe"           # add directory path as per the use-case
        os.startfile(fifapath)

    
    
    
    elif 'the time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f" Sir, the time is {strTime}")
    
    elif 'open code' in query:
    

        codepath= 'C:\\Users\\RAHUL DEB\\Microsoft VS Code\\Code.exe'       # add directory path as per the use-case
        os.startfile(codepath)
    
    elif 'open blender' in query:
         blenderpath= 'C:\\Program Files\\Blender Foundation\\Blender\\blender.exe'         # add directory path as per the use-case
         os.startfile(blenderpath)
     
    elif "news" in query:
                speak("Please wait while I fetch fresh news.")
                print("Please wait while I fetch fresh news.")
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = BeautifulSoup(xml_page, "html.parser")
                news_list = soup_page.findAll("item")
                speak("Here are top 5 news")
                print("Here are top 5 news")
                for news in news_list[:5]:
                    print(news.title.text)
                    speak(news.title.text)
                
     
 




     
     
     
    elif 'email to rahul' in query:
    
   
    
    
        try:
            speak("What should i say sir?")
            content= takeCommand()
            to="sendersmailaddress@gmail.com"  # add the senders mail address
            sendMail(to, content)
            speak("Email has been sent!")
            print("Email has been sent!")
        
     
        except Exception as e:
             print(e)
             speak("Sorry sir I am unable to send this email.")
             print("Sorry sir I am unable to send this email.")
     
    
     
    
     
    
    
    
    
    
    
       
    
    
    
        
        
        
    
    
    
    
    
