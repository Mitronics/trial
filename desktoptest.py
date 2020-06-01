import RPi.GPIO as GPIO
import time

buttonState = None
deviceState = None

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
GPIO.setup(buttons['L83_S'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttons['L83_P'], GPIO.OUT)

while True:
    
    print("Poczatek petli while")
    time.sleep(0.2)

    GPIO.output(buttons['L83_P'], GPIO.HIGH)

    buttonState = GPIO.input(buttons['START'])
    print('Stan przycisku przed nacisnieciem: ' + str(buttonState))

    GPIO.wait_for_edge(buttons['START'], GPIO.FALLING, bouncetime = 300) #oczekiwanie na wciśnięcie START

    buttonState = GPIO.input(buttons['START'])
    GPIO.output(buttons['L83_P'], GPIO.LOW)
    print('Stan przycisku po nacisnieciu: ' + str(buttonState))
    time.sleep(0.5)
    buttonState = GPIO.input(buttons['START'])
    print('Stan przycisku 0.5 sekundy po nacisnieciu: ' + str(buttonState))

    deviceState = GPIO.input(buttons['L83_S'])
    print('Stan akceptora przed podaniem banknotu: ' + str(deviceState))
    
    channel = GPIO.wait_for_edge(buttons['L83_S'], GPIO.RISING, timeout=20000, bouncetime = 300) #oczekiwanie na banknot

    if channel is None:
        print('timeout')
    else:
        deviceState = GPIO.input(buttons['L83_S'])
        print('Stan akceptora po podaniu banknotu: ' + str(deviceState))

