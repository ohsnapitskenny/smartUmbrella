import time

from neopixel import *
from random import randint

LEDS            = 12     # Aantel LEDS
PIN             = 18     # GPIO 18 / PIN 12
BRIGHTNESS      = 55     # min 0 / max 255

COLOR_R = randint(0, 255)
COLOR_G = randint(0, 255)
COLOR_B = randint(0, 255)

def loopLed(ring, color, wait_ms):

        for i in range(ring.numPixels()):
                ring.setPixelColor(i,color)
                ring.show()
                time.sleep(wait_ms/1000.0)
                ring.setPixelColor(i,0)
                ring.setPixelColor(i-1,0)

        for i in range(ring.numPixels()-1,-1,-1):
                ring.setPixelColor(i,color)
                ring.show()
                time.sleep(wait_ms/1000.0)
                ring.setPixelColor(i,0)
                ring.setPixelColor(i+1,0)

def resetLeds(ring, color, wait_ms=10):

        for i in range(ring.numPixels()):
                ring.setPixelColor(i, color)
                ring.show()

if __name__ == '__main__':

        ring = Adafruit_NeoPixel(LEDS, PIN, 800000, 5, False, BRIGHTNESS)

        ring.begin()

        for t in range (0, 5, 1):
                loopLed (ring, Color(COLOR_G, COLOR_R, COLOR_B), 100)

        resetLeds (ring,Color(0,0,0))