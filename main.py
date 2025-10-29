]import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pywhatkit
from googletrans import Translator
import os
import sys
import time
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)
recognizer = sr.Recognizer()
translator = Translator()
def speak(text, lang='en'):
if lang != 'en':
translated = translator.translate(text, dest=lang).text
print(f"[Translated → {lang}] {translated}")
engine.say(translated)
else:
print(f"Assistant: {text}")
engine.say(text)
engine.runAndWait()
def listen_command():
with sr.Microphone() as source:
print("\n
Listening...")
recognizer.pause_threshold = 1
audio = recognizer.listen(source, phrase_time_limit=6)
try:
print("
Recognizing...")
command = recognizer.recognize_google(audio, language='en-in')
print(f"
You said: {command}\n")
except sr.UnknownValueError:
speak("Sorry, I didn't catch that. Please say it again.")
return ""
return command.lower()
def run_jarvis():
speak("Hello, I am your AI desktop assistant. How can I help you today?")
while True:
command = listen_command()
if not command:
continue
if "hello" in command or "hi jarvis" in command:
speak("Hello! How are you?")
elif "how are you" in command:
speak("I am fine, thank you! What about you?")
elif "your name" in command:
speak("My name is Jarvis, your personal assistant.")
elif "stop" in command or "exit" in command or "quit" in command:
speak("Goodbye! Have a nice day.")
break
elif "time" in command:
current_time = datetime.datetime.now().strftime("%I:%M %p")
speak(f"The current time is {current_time}")
elif "date" in command:
today = datetime.date.today().strftime("%B %d, %Y")
speak(f"Today's date is {today}")
elif "youtube" in command:
speak("Opening YouTube...")
webbrowser.open("https://www.youtube.com")
elif "wikipedia" in command:
speak("Opening Wikipedia...")
webbrowser.open("https://www.wikipedia.org")
elif "instagram" in command:
speak("Opening Instagram...")
webbrowser.open("https://www.instagram.com")
elif "twitter" in command:
speak("Opening Twitter...")
webbrowser.open("https://www.twitter.com")
elif "linkedin" in command:
speak("Opening LinkedIn...")
webbrowser.open("https://www.linkedin.com")
elif "search" in command:
query = command.replace("search", "").strip()
speak(f"Searching Google for {query}")
pywhatkit.search(query)
elif "translate" in command:
speak("Please say the sentence you want to translate.")
text_to_translate = listen_command()
if "hindi" in command:
speak(text_to_translate, lang='hi')
elif "bhojpuri" in command:
speak(text_to_translate, lang='bho')
else:
speak("Please specify the language, like Hindi or Bhojpuri.")
elif "open notepad" in command:
speak("Opening Notepad...")
os.system("notepad")
elif "open calculator" in command:
speak("Opening Calculator...")
os.system("calc")
elif "restart" in command:
speak("Restarting system...")
os.system("shutdown /r /t 1")
elif "shutdown" in command:
speak("Shutting down system...")
os.system("shutdown /s /t 1")
elif "play song" in command or "play music" in command:
speak("Which song should I play?")
song = listen_command()
pywhatkit.playonyt(song)
speak(f"Playing {song} on YouTube.")
else:
speak("I'm not sure how to respond to that.")
if __name__ == "__main__":
try:
run_jarvis()
except KeyboardInterrupt:
speak("Goodbye! See you soon.")
sys.exit()