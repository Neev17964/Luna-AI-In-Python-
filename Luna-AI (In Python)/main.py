import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from newsapi import NewsApiClient
from googleapiclient.discovery import build
import random
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="Your News API"

def get_weather(location):
    api_key = "Your API"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Build the request URL
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    # If the API call is successful
    if data["cod"] == 200:
        main = data["main"]
        weather_description = data["weather"][0]["description"]
        temperature = main["temp"]
        humidity = main["humidity"]
        
        # Prepare the weather information as a spoken response
        weather_info = (
            f"The weather in {location} is {temperature}°C with {weather_description}. "
            f"The humidity is {humidity}%."
        )
    else:
        weather_info = f"Sorry, I couldn't find the weather for {location}."
    
    return weather_info

def speak (text):
    engine.say(text)
    engine.runAndWait()

# def aiProcess(command):
#     client = OpenAI(api_key="Your API",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named Luna skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content

def processCommand(c):
    # if "open google" in c.lower():
    #     webbrowser.open("https://google.com")

    # elif "open facebook" in c.lower():
    #     webbrowser.open("https://facebook.com")

    # elif "open youtube" in c.lower():
    #     webbrowser.open("https://youtube.com")

    # elif "open linkedin" in c.lower():
    #     webbrowser.open("https://linkedin.com")

    # elif "open instagram" in c.lower():
    #     webbrowser.open("https://instagram.com") 

    # elif "open gpt" in c.lower():
    #     webbrowser.open("https://chatgpt.com/")  

    if "open" in c.lower():
        location = c.split("open")[-1].strip()  # A better aprroach 
        word = location
        webbrowser.open(f"https://{word}.com")     

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        
        # Initialize NewsAPI client
        newsapi = NewsApiClient(api_key="Your API")  # Use correct format for API key

        # Fetch top headlines
        try:
            top_headlines = newsapi.get_top_headlines(language='en', country='us')

            # Print the first headline
            if top_headlines['articles']:
            # Get the first headline
                random_article = random.choice(top_headlines['articles'])
                headline = random_article['title']
                print(f"Headline: {headline}")
                speak(headline)  # Speak the headline
        except Exception as e:
            print(f"An error occurred: {e}")

    elif "weather" in c.lower():
        try:
            # Extract location from the input (assuming it's after the word "in")
            location = c.split("in")[-1].strip()
            
            # Get the weather information
            weather_info = get_weather(location)
            
            # Make Luna speak the weather info
            print(weather_info)
            speak(weather_info)
        except Exception as err:
            print(f"Sorry I can't  find the weather for that location")
            speak("Sorry I can't  find the weather for that location")

    elif "start" in c.lower():
         app_name = c.split("start")[-1].strip()
         open_app(app_name)
          
if  __name__ == "__main__":
    speak("Initializing Luna......")

    while True:
    # Listen for the Wakeup word "Jarvis"
    # Obtain audio from microphone
        r = sr.Recognizer()
        
        # Recognize speech using google
        print("Recognizing......")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=4, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "luna"):
                speak("yeah")
                # Listen for command
                with sr.Microphone() as source:
                    print("Luna Active.....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    if command.lower() == "close":
                        speak("Closing Luna......")
                        print("......CLOSING LUNA......")
                        break

                    print(command.upper())
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))