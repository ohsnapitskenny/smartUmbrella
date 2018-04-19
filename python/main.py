import time
from neopixel import *

# NeoPixel
LED_COUNT       = 12   # Number of LEDS
LED_PIN         = 18    # GPIO 18 / PIN 12
LED_FREQ_HZ     = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 10      # DMA channel to use for generating signal (try 10)
LED_INVERT      = False   # True to invert the signal (when using NPN transistor level shift)
LED_BRIGHTNESS  = 200     # Set to 0 for darkest and 255 for brightest

# FX
WAIT_MS = 40

# COLORS
BLUE = Color(95, 235, 225)

def expectsRain(ring, color, wait_ms=10):
    for t in range (0, 5, 1):
        colorWipe(ring, BLUE, WAIT_MS)
        colorWipe(ring, Color(0, 0, 0), WAIT_MS)

# ColorFX's
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

    for t in range (0, 5, 1):
        colorWipe(ring, Color(0, 0, 255), 50)
        colorWipe(ring, Color(0, 0, 0), 50)


    resetLeds(ring,Color(0,0,0))