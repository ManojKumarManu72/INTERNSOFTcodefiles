import speech_recognition as sr
import pyttsx3
import os
import time
import subprocess
import json
import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
print('**LOADING YOUR AI PERSONAL ASSISTANT**')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",'voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good morning")
        print("Hello, Goodmorning")
    elif hour >=12 and hour <=18:
        speak("Hello, Good afternoon")
        print("Hello, Good afternoon")
    elif hour >18 and hour<=21:
        speak("Hello, Good evening")
        print("Hello, Good evening")
    else:
        speak("Hello, Good night")
        print("Hello, Good night")
def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening....")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Please Repeat")
            return "None"
        return statement
speak("LOADING YOUR AI PERSONAL ASSISTANT")
wishMe()
if __name__=='__main__':
    while True:
        speak("How can i help you?")
        statement = Command().lower()
        if statement == 0:
            continue
        if "Good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal AI is Shutting down, Good bye!")
            print("**Your personal AI is Shutting down, Good bye!**")
            break
            
        if 'wikipedia' in statement:
            speak("Searching wikipedia...")
            statement = statement.replace("wikipedia"," ")
            results = wikipedia.summary(statement , sentences = 3)
            speak("According to wikipedia....")
            print(results)
            speak(results)
            
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open")
            time.sleep(5)
            
        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google search is open for you")
            time.sleep(5)
        elif "weather" in statement:
            api_key = "9780f4ee34bf12d62713c6f00f50764b"
            base_url ="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid = "+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" the temperature in kelvin units is " + str(current_temperature) +"\n humidity in percentage is" + str(current_humidity) + "\n weather description" + str(weather_description))
                print("the temperature in kelvin units is " + str(current_temperature) +"\n humidity in percentage is" + str(current_humidity) + "\n weather description" + str(weather_description))
            else:
                speak("City not found")
                print("City not found!!")
                    
        elif "time" in statement:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                          
        elif "who are you" in statement or "what can you do" in statement:
                    speak("Im Your Personal AI Assistant, im here to make your life easier, by taking commands from you")
                    print("Im Your Personal AI Assistant, im here to make your life easier, by taking commands from you")
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("You only Manoj Kumar S!")
                    print("You only Manoj Kumar S!")
                          
        elif "open stackoverflow" in statement:
                    webbrowser.open_new_tab("https://stackoverflow.com/login")
                    time.sleep(5)
                          
        elif "news" in statement:
                    news = webbrowser.open_new_tab("https://timesofindia.Indiatimes.com/home/headlines")
                    speak("The news for the day")
                    time.sleep(7)
                          
        elif "search" in statement:
                    statement = statement.replace("search"," ")
                    webbrowser.open_new_tab("statement")
                    time.sleep(5)
                          
                          
        elif "ask" in statement:
                    speak("I can answer to computational and geographical questions too just try me !! what do you want to ask ")
                    question = Command()
                    app_id = " RQKEAJ-27889QJKWA"
                    client = wolframalpha.Client('RQKEAJ-27889QJKWA')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)
                          
        elif "log off" in statement or "sign out" in statement or "shut down" in statement:
                    speak("Ok, Your PC will shut down, Good Bye")
                    subprocess.call(['shutdown',"/1"])
                          
                          
    time.sleep(5)