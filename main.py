from automation import *
from defs import *
import os.path
import cv2
import smtplib
import wikipedia
import pyjokes
import webbrowser
import speedtest
import random
import pyautogui
import cv2
from requests import *
from pywikihow import *

m = ["you asked for this song?", "playing" ,"go ask alexa!   ok fine wait", "here you go!"]
z = ["ok", "as you wish", "sure", "why not", "anything for you", "working on it", "1 sec", "requesting", "why should i do it for you?     ok fine"]
wish()
def main_():
    while True:
        query = takecommand()
        touch = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(touch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        button_state = GPIO.input(touch)
        try:
            if "what can you do" in query:
                speak("i can help to do lot many things like..")
                speak("i can tell you the current time and date,")
                speak("i can tell you the current weather,")
                speak("i can tell you battery and cpu usage,")
                speak("i can create the reminder list,")
                speak("i can shut down or logout or hibernate your system,")
                speak("i can tell you non funny jokes")
                speak("i can open any website,")
                speak("i can repeat what you told me,")
                speak("i can search anything on wikipedia,")
                speak("i have the full control over the electronic devices like light, keyboard and etc...")
                speak("i have a wake word detection i will be online if you say hey ADAM")
                speak("And yes one more thing, My mahn is working on this system to add more features...,")
                speak("so...tell me how can i help you?")
            elif "what are you" in query or "who are you" in query or "introduce" in query or "what is your name" in query:
                speak("I am ADAM!")
                speak("your virtual assistant")
                speak("and i am here to assist you with a variety of task since best i can")
                speak("i will be available 24 past 7 if i am powered on...... lol!")
                speak("i can help to do lot many things like..")
                speak("i can tell you the current time and date,")
                speak("i can tell you the current weather,")
                speak("i can tell you battery and cpu usage,")
                speak("i can create the reminder list,")
                speak("i can shut down or logout or hibernate your system,")
                speak("i can tell you non funny jokes")
                speak("i can open any website,")
                speak("i can repeat what you told me,")
                speak("i can search anything on wikipedia,")
                speak("i have the full control over the electronic devices like light, keyboard and etc...")
                speak("i have a wake word detection i will be online if you say hey ADAM")
                speak("And yes one more thing, My mahn is working on this system to add more features...,")
                speak("so...tell me how can i help you?")
            elif "off light" in query or "of light" in query or "off the light" in query or "of the light" in query:
                speak(random.choice(z))
                lig_off()
            elif "on light" in query or "on the light" in query:
                speak(random.choice(z))
                lig_on()
            elif "off keyboard" in query or "of keyboard" in query or "off the keyboard" in query or "of the keyboard" in query:
                speak(random.choice(z))
                key_off()
            elif "on keyboard" in query or "on the keyboard" in query:
                speak(random.choice(z))
                key_on()
            elif "off fan" in query or "of fan" in query or "off the fan" in query or "of the fan" in query:
                speak(random.choice(z))
                fan_off()
            elif "on fan" in query or "on the fan" in query:
                speak(random.choice(z))
                fan_on()
            elif "turn off everything" in query or "turn of everything" in query:
                speak(random.choice(z))
                everything_off()
            elif "charge tab" in query or "charge my tab" in query or "charge phone" in query or "charge my phone" in query:
                speak(random.choice(z))
                tab_on()
            elif "turn of the charger" in query or "turn off the charger" in query:
                speak(random.choice(z))
                tab_off()
            elif "turn on everything" in query:
                speak(random.choice(z))
                everything_on()
            elif "it's so cold" in query or "cold" in query:
                speak("i know right, !? shall i turn off the fan for you?")
                fan_off()
            elif "it's to dark" in query or "dark" in query:
                speak("is it so? ok  turning the light on")
                lig_on()
            elif "it's to sunny" in query or "sunny" in query or "Sunny" in query:
                speak("yeah")
                lig_off()
            elif "light and fan" in query or "fan and light" in query:
                speak(random.choice(z))
                lig_on()
                fan_on()
            elif "turn on the monitor" in query or "turn on monitor" in query or "turn on 3 pin" in query:
                speak(random.choice(z))
                pin_on()
            elif "off the monitor" in query or "of the monitor" in query or "off 3 pin" in query or "of 3 pin" in query:
                speak(random.choice(z))
                pin_off()
            elif "on the biglight" in query or "on the big light" in query or "on the tubelight" in query or "on the tube light" in query:
                speak(random.choice(z))
                on()
            elif "off the biglight" in query or "off the big light" in query or "off the tubelight" in query or "off the tube light" in query:
                speak(random.choice(z))
                off()
            elif "good morning" in query or "morning" in query:
                speak("morning")
                date()
                on()
                cpu()
                fan_off()
                tab_off()
            elif "get up" in query or "getup" in query:
                fan_off()
                on()
                speak("get up?!")
            elif "adios" in query:
                everything_off()
                speak(random.choice(goodbyes))
            elif "wakeup" in query or "wake up" in query or "make up" in query or "makeup" in query:
                speak(random.choice(greetings))
                speak("how's life?")
                if "good" in query:
                    speak("thats good to hear")
                elif "bad" in query:
                    speak("hmm sad for u.. lol")
            elif "good night" in query or "goodnight" in query:
                everything_off()
                fan_on()
                tab_on()
                speak("good night")
            elif "study mode" in query or "study" in query:
                speak(random.choice(z))
                everything_off()
                fan_on()
                lig_on()
            elif 'timer' in query or 'stopwatch' in query:
                speak("For how many minutes?")
                timing = takecommand()
                timing =timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                speak(f'I will remind you in {timing} minutes')
                timing = float(timing)
                timing = timing * 50
                sleep(timing)
                music_dir = 'https://www.youtube.com/watch?v=iNpXCzaWW1s'
                play(music_dir)
                sleep(10)
                speak("your time is finished .")
            elif 'cpu' in query or "CPU" in query:
                cpu()
            elif 'open map' in query:
                speak('tell me the location you are looking for')
                location = takecommand()
                url2 = 'https://google.nl/maps/place/' + location +'/&amp;'
                webbrowser.open(url2)
                speak('alliiya , the location is on your screen ')
            elif 'create a folder named' in query:
                Newfolder = query.replace("create a folder named", "")
                path= '/home/aj-17'
                os.chdir(path)
                os.makedirs(Newfolder)
                speak('i have  made a folder named ' +Newfolder+' in your home directry')
            elif "shut down" in query or "shutdown" in query or "power off" in query or "poweroff" in query or "power of" in query or "powerof" in query:
                speak("ok then .... it was nice talking and working for you")
                speak(random.choice(goodbyes))
                everything_off()
                os.system("init 0")            
            elif "reboot" in query or "Reboot" in query:
                speak(random.choice(z))
                everything_off()
                os.system("init 6")
            elif "update" in query or "upgrade" in query:
                speak(random.choice(z))
                os.system("sudo apt-get update")
                os.system("sudo apt-get upgrade -y")
                speak("the latest update is installed in your computer.... rebooting the computer is recommended")
            elif "play" in query:
                query = query.replace("play","")
                play(query)
                speak(random.choice(m))
                speak(f"playing: {query}")
            elif "how to make" in query:
                speak(random.choice(z))
                query = query.replace("how to make","how to make")
                yt = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(yt)
                speak(f"playing {query}")
            elif "youtube" in query or "Youtube" in query:
                speak(" what should i search on youtube?")
                cm = takecommand().lower()
                if "nothing" in cm or "just open" in cm:
                    webbrowser.open(f"https://www.youtube.com/")
                    speak("opening youtube")
                else:
                    webbrowser.open(f"https://www.youtube.com/results?search_query=" + cm)
                    speak(f" wait for 2 second, searching for {cm} in youtube...")
            elif 'tell' in query:
                audio_data = query.replace('tell me', '')
                calculate(audio_data)
            elif "ip address" in query or "IP address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
            elif "set alarm" in query:
                time2 = datetime.datetime.now().strftime('%H')
                speak("please enter the time")
                nn = int(datetime.datetime.now().hour)
                if nn==time: 
                    music_dir = 'https://www.youtube.com/watch?v=iNpXCzaWW1s'
                    play(music_dir)
            elif "google" in query or "Google" in query:
                speak(" what should i search on google?")
                cm = takecommand().lower()
                if "nothing" in cm or "just open" in cm:
                    webbrowser.open(f"https://google.com/")
                    speak("opening google")
                else:
                    webbrowser.open(f"https://google.com/search?q=" + cm)
                    speak(f" wait for 2 second, searching for {cm}...")
            elif "camera" in query:
                try:
                    speak(random.choice(z)) 
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k==27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()
                except Exception as e:
                    print(e)
            elif "maths textbook" in query:
                mt = 'https://www.shaalaa.com/textbook-solutions/selina-solutions-concise-mathematics-class-9-icse_143'
                webbrowser.open(mt)
                speak("opening maths texbook")
            elif "thanks" in query or "thank you" in query:
                speak("the pleasure is mine")
            elif "show me" in query:
                speak(random.choice(z))
                query = query.replace("ADAM","")
                query = query.replace("show me","")
                sm = 'https://google.com/search?q=' + query
                webbrowser.open(sm)
                speak(f"opening google to show you {query}")
            elif "i want to see" in query:
                speak(random.choice(z))
                query = query.replace("ADAM","")
                query = query.replace("i want to see","")
                sm = 'https://google.com/search?q=' + query
                webbrowser.open(sm)
                speak(f"opening google to show you {query}")
            elif "open" in query:
                speak(random.choice(z))
                query = query.replace("ADAM","")
                query = query.replace("open","")
                webbrowser.open(f"https://google.com/search?q=" + query)
                speak(" wait for 2 second, opening " + query)
            elif "internet speed test" in query:
                speak(random.choice(z))
                st = speedtest.Speedtest()
                dl = (round(st.download()/1000000, 2))
                up = (round(st.upload()/1000000, 2))
                speak(f" we have {dl} Mbps dowloading speed....")
                speak(f"and {up} Mbps uploading speed....")
            elif "switch the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                speak("switching the window")
                pyautogui.keyUp("alt")
            elif "close the tab" in query:
                pyautogui.keyDown("Ctrl")
                pyautogui.press("W")
                speak("closing the tab")
                pyautogui.keyUp("Ctrl")
            elif "close the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                speak("closing the window")
                pyautogui.keyUp("alt")
            elif 'search wikipedia' in query:
                speak("searching wikipedia")
                query = query.replace("ADAM","")
                query = query.replace("search wikipedia","")
                wiki = wikipedia.summary(query,2)
                speak("accrording to wikipedia : ")
                speak({wiki})
            elif 'when was' in query or 'what is' in query or 'who is' in query:
                speak("searching wikipedia")
                query = query.replace("ADAM","")
                wiki = wikipedia.summary(query,2)
                speak("accrording to wikipedia : ")
                speak({wiki})
            elif "discord" in query:
                webbrowser.open("https://discord.com/channels/@me")
                speak("on it")
            elif "gmail" in query:
                webbrowser.open("mail.google.com")
                speak(random.choice(z))
            elif "classroom" in query:
                webbrowser.open("https://classroom.google.com/u/0/")
                speak(random.choice(z))
            elif "meet" in query:
                webbrowser.open("meet.google.com")
                speak(random.choice(z))
            elif "joke" in query:
                speak("here you go a non funny joke, lol")
                joke = pyjokes.get_joke()
                speak(joke)
            elif "where am i" in query or "location" in query or "where are we" in query:
                speak("wait , let me check")
                ipAdd = get('https://api.ipify.org').text
                print(ipAdd)
                url = get('https://get.geojs.io/v1/ip/geo/59.93.250.207.json').text
                geo_requests = request.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f" i am not sure, but i think we are in {city} in {state} of {country}")
            elif "remember" in query:
                rememberMsg = query.replace("remember that","")
                rememberMsg = rememberMsg.replace("ADAM", "")
                speak("the reminder is:" + rememberMsg)
                remeber = open('data.txt','w')
                remeber.write(rememberMsg)
                remeber.close()
            elif "do I have" in query:
                with open('data.txt') as f:
                    lines = f.read()
                    speak(f" you told me to remember this: {lines}")
            elif "how much power we have" in query or "how much power left" in query or "battery" in query:
                battery = psutil.sensors_battery()
                percentage = battery
                speak(f" our system have {percentage} percent battery")
            elif "take screenshot" in query or "take a screenshot" in query:
                speak(", please tell me the name for this screenshot file")
                name = takecommand().lower()
                speak("please  hold the screen for 2 second, i am taking a screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done , the screenshot is saved in our main folder")
            elif "how to" in query:
                how = query.replace("how to","how to")
                max_result = 1
                lang = 'en'
                how_to = search_wikihow(how,max_result,lang)
                speak(how_to[0].summary)
            elif button_state == True:
                    on()
                    while GPIO.input(touch) == False:
                            sleep(0.2)
                    else:
                            off()
            elif "time" in query:
                time()
            elif "date" in query:
                date()
            elif "hai" in query or "hi" in query or "hey" in query or "sup" in query:
                speak(random.choice(greetings))
                speak("how's life?")
                if "good" in query:
                    speak("shaa y da it should be bad know!")
                elif "bad" in query:
                    speak("finally some peace for me..")
                else:
                    pass
            elif "how's ur life" in query or "how's life" in query:
                speak("life was good before u made me... ")
                speak("no offence... lol")
            elif "boring" in query:
                speak('wait let me think of an idea')
                p = 'top english songs of all time'
                play(p)
                sleep(2)
                speak("top english songs")
                speak("let's listen to mosic?! lol")
            elif "bye" in query or "buy" in query or "break" in query or "sleep" in query:
                speak("ok ....  you can wake me up by clicking the touch id")
                speak(random.choice(goodbyes))
                everything_off()
                break;
            elif "rest in peace" in query or "peace" in query:
                speak("ok")
                speak("thank you for using me")
                of()
            elif "version" in query:
                speak("my current version is 5 . 3 . 7")
            elif "who made you" in query:
                speak("i was made by Aaron Jophy at may 1st 2020")
            elif "why did he make you" in query:
                speak("he made me so that i can help him in many things and to make his life easier")
            elif "aaron" in query or "iron" in query or "arin" in query:
                speak("he is my man")
                speak("he created me...")
            elif 'repeat' in query:
                voice_data = query.replace("repeat", "")
                voice_data = query.replace("that", "")
                speak(voice_data)
            elif "what do you do in your free time" in query or "free time" in query:
                speak("hmm i listen to your conversation.... lol")


                            
        except Exception as e:
            print(e)
            speak("pardon me...")
main_()
