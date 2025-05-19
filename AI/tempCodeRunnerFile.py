import pyttsx3 #!pip install pyttsx3
import speech_recognition as sr #!pip install SpeechRecognition

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate')
    engine.setProperty('rate', rate=50)
    volume=engine.setProperty('volume') 
    engine.setProperty('volume', volume+0.25)
    return engine

def speak():
    engine = initialize_engine()
    engine.say("Hello, I am your assistant. How can I help you today?")
    engine.runAndWait()

speak("Hello, I'm Mishu")