import time

from neopixel import *
from random import randint

LED_COUNT       = 12   # Number of LEDS
LED_PIN         = 18    # GPIO 18 / PIN 12
LED_FREQ_HZ     = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA        = 5      # DMA channel to use for generating signal (try 10)
LED_DMA         = 10      # DMA channel to use for generating signal (try 10)
LED_INVERT      = False   # True to invert the signal (when using NPN transistor level shift)
LED_BRIGHTNESS  = 255     # Set to 0 for darkest and 255 for brightest

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

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def resetLeds(ring, color, wait_ms=10):
    for i in range(ring.numPixels()):
        ring.setPixelColor(i, color)
        ring.show()

if __name__ == '__main__':

    ring = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    ring.begin()

    for t in range (0, LED_COUNT, 1):
        # loopLed(ring, Color(0, 0, 255), 100)
        colorWipe(ring, Color(0, 0, 255), 10)
        colorWipe(ring, Color(0, 0, 0), 10)


    resetLeds(ring,Color(0,0,0))