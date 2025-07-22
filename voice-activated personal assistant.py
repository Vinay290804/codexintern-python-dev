import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import json
from time import sleep

# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Weather API key (in a real app, use environment variables)
WEATHER_API_KEY = "your_api_key_here"

def speak(text):
    """Convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except Exception as e:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None

def get_weather(city="New York"):
    """Get weather information"""
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={WEATHER_API_KEY}&q={city}"
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data["main"]
            temp = main["temp"] - 273.15  # Convert Kelvin to Celsius
            weather_desc = data["weather"][0]["description"]
            return f"Weather in {city}: {weather_desc}, Temperature: {temp:.1f}°C"
        else:
            return "City not found. Please try again."
    except:
        return "Sorry, I couldn't fetch the weather right now."

def personal_assistant():
    """Main assistant function"""
    speak("Hello! I'm your personal assistant. How can I help you today?")
    
    while True:
        query = listen()
        
        if not query:
            continue
            
        if 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break
            
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
            
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
            
        elif 'reminder' in query or 'remind me' in query:
            speak("What should I remind you about?")
            reminder = listen()
            speak(f"Okay, I'll remind you to {reminder}")
            # In a real app, you would schedule this reminder
            
        elif 'weather' in query:
            speak("Which city's weather would you like to know?")
            city = listen()
            if city:
                weather_info = get_weather(city)
                speak(weather_info)
            else:
                speak("I'll check the weather for New York")
                speak(get_weather())
                
        elif 'news' in query:
            speak("Here are the latest headlines")
            # In a real app, you would fetch news from an API
            headlines = [
                "Scientists discover new species in Amazon rainforest",
                "Tech company announces breakthrough in quantum computing",
                "Global leaders meet to discuss climate change"
            ]
            for i, headline in enumerate(headlines, 1):
                speak(f"Headline {i}: {headline}")
                sleep(1)
                
        elif 'search' in query or 'google' in query:
            speak("What would you like me to search for?")
            search_term = listen()
            if search_term:
                url = f"https://google.com/search?q={search_term}"
                webbrowser.get().open(url)
                speak(f"Here are the search results for {search_term}")
                
        elif 'thank you' in query:
            speak("You're welcome! Is there anything else I can help with?")
            
        else:
            speak("I'm not sure I understand. Could you try asking differently?")

if _name_ == "_main_":
    personal_assistant()