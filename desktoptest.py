import RPi.GPIO as GPIO
import time

buttonState = None

##  STATUSY
global StatusDev
StatusDev = {}
StatusDev['Start'] = 0

#0 - czeka na guzik
#1 - START TESSTU
StatusDev['currentState'] = 0
StatusDev['reboot'] = 0
StatusDev['ReceiveSNVer']=0
    
StatusDev['StartADBProcedure'] = 0
StatusDev['ADBAnalize'] = 0
StatusDev['TimeoutThanks'] = -2

global buttons
buttons ={}
#zielony - START - 5 
#niebieski - LANG - 10
#przyciski w ADBL_UA sa podlaczone pod piny:
#B0 - 16
#B1 - 22
#B2 - 24
#B3 - 26
#B4 - 28
#B5 - 32
buttons['START'] = 32   # pin 32 Button5
buttons['ENABLE'] = 1
#sygnal z czytnika banknotow L83 jest podlaczony pod pin 18:
buttons['L83_S'] = 18   # pin 18 input for L83 signals
#sterowanie zasilaniem czytnika banknotow L83 odbywa się przez pin 10:
buttons['L83_P'] = 10   # pin 18 output for powering L83
   
buttons['START_press'] = 0   # GPIO_66

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttons['START'],GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttons['L83_S'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttons['L83_P'], GPIO.OUT)

while True:
    print("Petla while")
    time.sleep(0.2)
    GPIO.output(buttons['L83_P'], GPIO.LOW)
    buttonState = GPIO.input(buttons['START'])
    print(buttonState)
    GPIO.wait_for_edge(buttons['START'], GPIO.RISING) #oczekiwanie na wciśnięcie START
    buttons['START_press'] = 1
    if(StatusDev['Start']==0):
        StatusDev['Start']=1

    i2cConfButton['ButtonWatch']=0
    GPIO.output(buttons['L83_P'], GPIO.HIGH)
    buttonState = GPIO.input(buttons['START'])
    print(buttonState)
    channel = GPIO.wait_for_edge(buttons['L83_S'], GPIO.RISING, timeout=20000) #oczekiwanie na banknot
    if channel is None:
        SlupekGUI.BackToStart()
    else:
        if(StatusDev['currentState']==0):
            StatusDev['currentState']=1
            time.sleep(4)
