import sys
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 256)

import TextLed

def on():
    # every mutliples of 32 are first pixel
    for i, led in enumerate(TextLed.getLeds("AIRBUS")):
        pixels[i] = led

def px():
    # swift on first led in red just for test
    pixels[0] = (20, 0, 0)

def off():
    pixels.fill((0, 0, 0))

if __name__ == "__main__":
    globals()[sys.argv[1]]()
