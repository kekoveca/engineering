import RPi.GPIO as GPIO
import spidev
import numpy
import time

spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC have been initialized")


def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")


def getAdc():
    adcResponse = spi.xfer2([0, 0])
    adc = ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

    return adc


initSpiAdc()
measure = []
st0 = time.time()
st = time.time()
while st - st0 < 60: #здесь достаточно поменять одну цифру, чтобы изменить время, в течение которого измерялось давление
    st = time.time()
    measure.append(getAdc())
deinitSpiAdc()
k = len(measure)
measure = map(str, measure)
with open("/home/gr104/Desktop/Scripts/chel2spok.txt","w") as outfile:  # запись файлов, точно также, просто меняем название файла
    outfile.write("\n".join(measure))

