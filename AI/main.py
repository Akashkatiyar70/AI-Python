import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib,ssl
import openai_request as ai




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = ""
    while content == "":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("You Said......" + content)
        except Exception as e:
            print("Please try again....")

    return content

def main_process():
    while True:
        request = command().lower()
        if "Hello" in request:
            speak("Welcome to the voice assistant")
        elif "play music" in request:
            speak("Playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=-VdocEDizbA")
            elif song ==2:
                webbrowser.open("https://www.youtube.com/watch?v=jqOuWRtgsXU")
            elif song ==3:
                webbrowser.open("https://www.youtube.com/watch?v=K5bP-nYmUwU&list=RDK5bP-nYmUwU&start_radio=1&rv=ceUvteucN1c")
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is"+str(now_time))
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is"+str(now_time))
        elif "new task" in request:
            task = request.replace("new task", "")
            task= task.strip()
            if task != "":
                speak("Adding task :"+ task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open ("todo.txt", "r") as file:
                speak("Work we have to do today is : " + file.read())
        elif "so work" in request:
            with open ("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title="Today's works",
                message=tasks   
            )    
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            request = request.replace("AI", "")
            request = request.replace("search wikipedia", "")
            result=wikipedia.summary(request,sentences=2)
            speak(result)

        elif "search google" in request:
            request = request.replace("AI", "")
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q=" + request)

        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+919999999999", "Hello, this is a test message", 12, 3,30)
        
        # elif "send email" in request:
        #     pwk.send_mail("ammodelcontact@gmail.com", user_config.gmail_password, "hello","Hello, how ar you" , "Katiyarakash271@gmail.com") 
        #     speak("Email sent successfully")
        elif "send email" in request:   
            s= smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("ammodelcontact@gmail.com", user_config.gmail_password,)
            message = """Hello, how are you?"""
            s.sendmail("ammodelcontact@gmail.com","katiyarakash271@gmail.com", message)
            s.quit()
            speak("Email sent successfully")
        
        elif "ask ai" in request:
            request = request.replace("AI", "")
            request = request.replace("ask ai", "")
            response = ai.send_request(request)
            speak(response)
        else:
            ai_chat = []
            request = request.replace("AI", "")            

            print(request)
            ai_chat.append({"role": "user", "content": request})
            response = ai.send_request(request)
            print(response)
            speak(response)
main_process()
# speak("Hello, how are you?")