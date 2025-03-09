# Voice-Activated Personal Assistant
This is a Python-based voice-activated personal assistant that can recognize voice commands, fetch weather updates, read the latest news, and set reminders. The assistant uses speech recognition and text-to-speech features for an interactive experience.
# Features

- Speech Recognition: Converts spoken commands into text using Google Speech API.

- Text-to-Speech: Uses pyttsx3 for verbal responses.

- Weather Updates: Fetches real-time weather information using OpenWeatherMap API.

- News Updates: Retrieves top news headlines using RSS feeds.

- Reminders: Allows users to set reminders for tasks at specific times.

# Requirements
Ensure you have Python installed along with the following dependencies:

pip install speechrecognition pyttsx3 requests feedparser pyaudio

# usage
1.Run the script

     python app.py

2.Give voice commands such as:

- "What's the weather in New York?"

- "Tell me the news."

- "Set a reminder to call John at 5 PM."

- "Exit" to stop the assistant.

# configuation
Replace your_openweathermap_api_key in the script with your actual OpenWeatherMap API key.
