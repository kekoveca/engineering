import jetFunctions as j

import spidev
import time
import RPi.GPIO as GPIO
import numpy as np

directionPin = 27
enablePin = 22
stepPin = 17

spi = spidev.SpiDev()

j.initSpiAdc()
j.initStepMotorGpio()
try:
    measure = []
    for i in range (100):
        j.stepForward(9)
        measure.append(j.getAdc())
    j.save(measure, 100)    

finally:
    j.deinitSpiAdc()
    j.stepBackward(900)
