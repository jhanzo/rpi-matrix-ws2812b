import os
from PIL import ImageFont, Image, ImageDraw

"""
you can edit gbd file with a free tool like gbdfed
then convert gbd to pil with a simple python script like pilfont.py
"""

def getLeds(text):
    image = Image.new("RGB", (32, 8), "#001F5B")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load("./fonts/big.pil")
    draw.text((2, 1), text, (255, 255, 255), font=font)
    px = image.load()

    leds = []
    for y in range(8):
        for x in range(32):
            leds.append(px[x, y])

    return leds
    #return [px[x, y] for x in range(32) for y in range(8)]
