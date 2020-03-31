import sys
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 256)

from .text import TextLed

def on():
    # every mutliples of 32 are first pixel
    pixels = TextLed("Airbus")

def test():
    # swift on first led in red just for test
    pixels[0] = (20, 0, 0)

def off():
    pixels.fill((0, 0, 0))

if __name__ == "__main__":
    globals()[sys.argv[1]]()