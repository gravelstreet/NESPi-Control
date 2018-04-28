#!/etc/systemd/system python3

# NESPi Control Script V-1.1 alpha
# Author: beimklabautermann@mail.de
# Date: 04/28/2018

# Autostart: sudo systemctl enable nespi.py

import os
import RPi.GPIO as GPIO
from time import sleep


def ConfigButton(show)
    # Frequenc to check Buttons
    checkButton = 0.5

    # GPIO-Mode (GPIO.BCM / GPIO.Board)
    GPIO.setmode(GPIO.BCM)

    # GPIO-/ Board-Pin to power Board
    powerButton = 23

    # GPIO-/ Board-Pin to reset Board
    resetButton = 24

    # GPIO-/ Board-Pin to load capacitor
    capacitor = 25

    # GPIO-Setup
    GPIO.setwarnings(False)
    GPIO.setup(powerButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(resetButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    if capacitor:
        GPIO.setup(capacitor, GPIO.OUT)
        GPIO.output(capacitor, GPIO.HIGH)
        sleep(2)

    if show:
        print('\tFrequenc to check Buttons:\t\t{}'.format(checkButton))
        print('\tGPIO-Mode:\t\t\t\t{}'.format(GPIO.setmode))
        print('\tGPIO-/ Board-Pin to power Board:\t{}'.format(powerButton))
        print('\tGPIO-/ Board-Pin to reset Board:\t{}'.format(resetButton))
        print('\tGPIO-/ Board-Pin to load capacitor:\t{}'.format(capacitor))

return(checkButton, powerButton, resetButton)


def ConfigFan(checkButton, show):
    # CPU-Temperature to power Fan off
    cpuTemp[1] = 40

    # CPU-Temperature to power Fan on
    cpuTemp[2] = 55

    # Frequenc to check CPU-Temperature
    checkTemp = 20

    # Duration of Fan-Annimation
    fanAct = 20

    # GPIO-/ Board-Pin to control Fan
    powerFan = 18

    # GPIO-Setup
    GPIO.setup(powerFan, GPIO.OUT)

    if checkTemp/checkButton > 1:
        turns = round(checkTemp/checkButton)
    else:
        turns = 1

    if show:
        print('\tCPU-Temperature to power Fan off:\t{}'.format(cpuTemp[1]))
        print('\tCPU-Temperature to power Fan on:\t{}'.format(cpuTemp[2]))
        print('\tFrequenc to check CPU-Temperature:\t{}'.format(checkTemp))
        print('\tDuration of Fan-Annimation:\t\t{}'.format(fanAct))
        print('\tGPIO-/ Board-Pin to control Fan:\t{}'.format(powerFan))

return(turns, cpuTemp, powerFan, fanAct)


def pushButton(press)
    os.system('sudo shutdown -h now', 'sudo reboot now')[press]
    print('Shutting down', 'Resetting', end='')[press, 2]

    for count in range(3):
        print(end='.')
        sleep(0.5)
        
return()


def getTemp(show):
    meas = os.popen('vcgencmd measure_temp').readline()
    temp = int(meas.replace("temp=", "").replace("'C\n", ""))

    if show:
        print('CPU-Temperature: ', end=meas.replace("temp=", ""))

return(temp)


def writeFan(power, loops):
    print('Fan powered off', 'Fan powered on', end='\t')[power, 2]

    if loops:
        for count in range(loops):
            print('|', '/', '-',  '\\', end='\b')[count-floor(count/4)*4, 4]

            if power:
                sleep(((count+1)*2)^-1)
            else:
                sleep((count+1)*0.05)

    print()
return()


[Wait, PwrBtn, RstBtn] = ConfigButton(False)
[Turns, Temp, PwrFan, FanAct] = ConfigFan(Wait, False)

while True:
    for Count in range(Turns):
        if ~GPIO.input(PwrBtn) or ~GPIO.input(RstBtn):
            pushButton(GPIO.input(PwrBtn))
        else:
            sleep(Wait)

    Temp[0] = getTemp(False)

    if Temp[0] < Temp[1] and GPIO.output(PwrFan) or Temp[0] > Tenp[2] and ~GPIO.output(PwrFan):
        GPIO.output(PwrFan) = ~GPIO.output(PwrFan)
        writeFan(GPIO.output(PwrFan), FanAct)
