from gpiozero import LED
# import GPIO and time
import RPi.GPIO as GPIO

# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)#
GPIO.setup(20,GPIO.OUT)#
GPIO.setup(21,GPIO.OUT)#
GPIO.setup(12,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)#
GPIO.setup(8,GPIO.OUT)#
GPIO.setup(25,GPIO.OUT)#

led_up = LED(26)

#center leds on
def led_on():
    led_up.on()
#center leds off
def led_off():
    led_up.off()
#on light
def lig_on():
    GPIO.output(16,False)
#off light
def lig_off():
    GPIO.output(16,True)
#on keyboard
def key_on():
    GPIO.output(20,False)
#off keyboard
def key_off():
    GPIO.output(20,True)
#on fan
def fan_on():
    GPIO.output(21,False)
#off fan
def fan_off():
    GPIO.output(21,True)
#on tab
def tab_on():
    GPIO.output(25,False)
#off tab
def tab_off():
    GPIO.output(25,True)
#on mon
def pin_on():
    GPIO.output(7, False)
#off mon
def pin_off():
    GPIO.output(7, True)
#on speaker
def on():
    GPIO.output(8, False)
#off speaker
def off():
    GPIO.output(8, True)


def everything_off():
    GPIO.output(16,True)
    GPIO.output(20,True)
    GPIO.output(21,True)
    GPIO.output(12,True)
    GPIO.output(8,True)
    GPIO.output(7,True)
    GPIO.output(8,True)
    GPIO.output(1,True)
    GPIO.output(25,True)
def everything_on():
    GPIO.output(16,False)
    GPIO.output(20,False)
    GPIO.output(21,False)
    GPIO.output(12,False)
    GPIO.output(8,False)
    GPIO.output(7,False)
    GPIO.output(8,False)
    GPIO.output(1,False)
    GPIO.output(25,False)


