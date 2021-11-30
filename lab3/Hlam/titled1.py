import waveFunctions as b
import spidev
import time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time

spi = spidev.SpiDev()
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
b.initSpiAdc()
t0 = time.time()
t = t0
measure = []
while t - t0 < 10:
    t = time.time()
    measure.append(b.getAdc())


measure_x = []
b.waitForOpen()
if b.waitForOpen():
    t0 = time.time()
    t = t0
    while t - t0 < 15:
        t = time.time()
        measure_x.append(b.getAdc())

b.deinitSpiAdc()


