import speech_recognition as sr
import pyttsx3
import requests
import feedparser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Error connecting to speech recognition service"

def get_weather(city):
    api_key = "46f1c46ccc8bac8036819f33e0bb6ff3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        return f"The temperature in {city} is {temperature}°C with {description}."
    return "Sorry, I couldn't fetch the weather."

def get_news():
    news_feed = feedparser.parse("https://news.google.com/rss")
    headlines = [entry.title for entry in news_feed.entries[:5]]
    return "Here are today's top news headlines: " + ", ".join(headlines)

def set_reminder(task, time):
    reminder_time = datetime.datetime.strptime(time, "%H:%M").time()
    return f"Reminder set for {task} at {reminder_time.strftime('%I:%M %p')}"

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if "weather" in command:
            speak("Which city's weather would you like to know?")
            city = recognize_speech()
            weather_info = get_weather(city)
            speak(weather_info)
        elif "news" in command:
            news = get_news()
            speak(news)
        elif "reminder" in command:
            speak("What should I remind you about?")
            task = recognize_speech()
            speak("At what time?")
            time = recognize_speech()
            reminder = set_reminder(task, time)
            speak(reminder)
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
