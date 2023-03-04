import pyttsx3
import speech_recognition as sr
import pyaudio
from automation import *
from time import *
import datetime
import psutil
import wolframalpha
import sys
import os
import webbrowser as web
import requests
import random

greetings = ["hello", "what's up?!", "sup", "hey", "holla"]
goodbyes = ["bye", "goodbye", "see ya later", "adios"]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)    # Speed percent
engine.setProperty('volume', 0.9) 
##print(voices)
engine.setProperty('voices', voices[0].id)

#texttospeech
def speak(audio):
    led_on()
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    led_off()
def  takecommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            led_on()
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=6)

        try:
            print("Recognizing...")
            led_off()
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            print("Say that again please...")
            return "none"
        return query
    except Exception as e:
        print(e)
        speak("there was one error., please wait...")
        sleep(5)
        
def wish():
    everything_off()
    strTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=5:
        speak(random.choice(greetings))
        speak(" i am ADAM.")
        speak(f"it's {strTime} A.M")
    elif hour>=5 and hour<=6:
        lig_on()
        speak(random.choice(greetings))
        speak(" i am ADAM.")
        speak(f"it's {strTime} A.M")
    elif hour>=7 and hour<=9:
        lig_off()
        speak(random.choice(greetings))
        speak(" i am ADAM.")
        speak(f"it's {strTime} A.M")
        speak("what is your plan for the day?")
    elif hour>=9 and hour<=12:
        speak(random.choice(greetings))
        speak(" i am ADAM.")
        speak(f"it's {strTime} A.M")
        speak("how may i help you?")
    elif hour>12 and hour<18:
        speak(random.choice(greetings))
        speak(" i am ADAM.")
        speak(f"it's {strTime} P.M")
        speak("how may i help you?")
    elif hour>=18 and hour<22:
        lig_on()
        speak(random.choice(greetings))
        speak(" i am ADAM.")
        speak(f"it's {strTime} P.M")
        speak("how may i help you?")
    else:
        speak(random.choice(greetings))
        speak(", i am ADAM.")
        #lig_on()
        speak(f"it's {strTime} P.M")
        speak("how may i help you?")
    pin_on()
def time():
    strTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=5:
        speak(f"it's {strTime} A.M")
        speak("you must be sleeping!?")
    elif hour>= 5 and hour<= 6:
        speak(f"it's {strTime} A.M")
        lig_on() 
        speak("have a good day ")
    elif hour>= 7 and hour< 12:
        speak(f"it's {strTime} A.M")
        speak("have a good day sir.")
    elif hour>= 12 and hour< 18:
        speak(f"it's {strTime} P.M")
        speak("are you having a good day?")
    elif hour>= 18 and hour< 22:
        speak(f"it's {strTime} P.M")
        lig_on()
    elif hour>= 22 and hour<0:
        speak(f"it's {strTime} P.M")
        speak("and i do not think you should be wake at this hour")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"Sir, today's  date is {date} , month is {month} and year is {year}")

def touch():
    touch = 13
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print ("go ahead")
    while True:
            button_state = GPIO.input(touch)
            if button_state == True:
                    print("adam is activated")
                    main_()
                    while GPIO.input(touch) == True:
                            sleep(0.2)
                    else:
                            print("try agin")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)

def calculate(audio_data):
    app_id = '8REQUG-YQ7JGY96T8'
    client = wolframalpha.Client(app_id)
    res = client.query(audio_data)
    answer = next(res.results).text
    speak(answer)

def of():
    everything_off()
    os.system("init 0")
    
def reboot():
    everything_off()
    os.system("init 6")

def playonyt(topic: str, use_api: bool = False, open_video: bool = True) -> str:
    """Play a YouTube Video"""
    # use_api uses the pywhatkit playonyt API to get the url for the video
    # use the api only if the function is not working properly on its own

    if use_api is True:
        response = requests.get(
            f"https://pywhatkit.herokuapp.com/playonyt?topic={topic}")
        if open_video:
            web.open(response.content.decode('ascii'))
        return response.content.decode('ascii')
    else:
        url = 'https://www.youtube.com/results?q=' + topic
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count - 5] == "/results":
            raise Exception("No video found.")

        # print("Videos found, opening most recent video")
        if open_video:
            web.open("https://www.youtube.com" + lst[count - 5])
        return "https://www.youtube.com" + lst[count - 5]

def play(term):
    result = "https://www.youtube.com/results?search_query=" + term
    #web.open(result)
    playonyt(term)
    
def Paass(pass_inp):
    passw = "Aaron"
    pasw = str(passw)
    if pasw==str(pass_inp):
        speak("access granted")
        wish()
        #task()
    else:
        speak("access denied")
        speak("enter the correct id")

def execution():
    speak("I am protected by a password")
    #main_()
    while True:
        #pas = takecommand()
        pas = input("password pls:  ")
    Paass(e.get())
