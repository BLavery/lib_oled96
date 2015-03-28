#!/usr/bin/env python

# RASPBERRY PI VERSION

# NOTE: You need to have PIL installed for your python at the Pi

from lib_oled96 import ssd1306
from time import sleep
from PIL import ImageFont, ImageDraw, Image
font = ImageFont.load_default()


from smbus import SMBus                  #  These are the only two variant lines !!
i2cbus = SMBus(1)                        #
# 1 = Raspberry Pi but NOT early REV1 board

oled = ssd1306(i2cbus)
draw = oled.canvas   # "draw" onto this canvas, then call display() to send the canvas contents to the hardware.


# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = oled.height - padding - 1
# Draw a rectangle of the same size of screen
draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
# Move left to right keeping track of the current x position for drawing shapes.
x = padding

# Draw an ellipse.
draw.ellipse((x, top, x+shape_width, bottom), outline=1, fill=0)
x += shape_width + padding
# Draw a filled rectangle.
draw.rectangle((x, top, x+shape_width, bottom), outline=1, fill=1)
x += shape_width + padding
# Draw a triangle.
draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=1, fill=0)
x += shape_width+padding
# Draw an X.
draw.line((x, bottom, x+shape_width, top), fill=1)
draw.line((x, top, x+shape_width, bottom), fill=1)
#x += shape_width+padding

# Load default font.
font = ImageFont.load_default()

# Nah, second thoughts ... Alternatively load another TTF font.

font = ImageFont.truetype('FreeSerif.ttf', 15)


oled.display()
sleep(3)

# Write two lines of text.
draw.text((x, top),    'Hello',  font=font, fill=1)
draw.text((x, top+40), 'World!', font=font, fill=1)
oled.display()
sleep(3)
draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=255, fill=1)
oled.display()
sleep(3)
logo = Image.open('pi_logo.png')
draw.bitmap((32, 0), logo, fill=0)

oled.display()
sleep(3)
draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
font = ImageFont.truetype('FreeSerifItalic.ttf', 57)
draw.text((18, 0), 'A5y', font=font, fill=1)
oled.display()

sleep(3)
draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
font = ImageFont.truetype('FreeSans.ttf', 10)
draw.text((0, 0), 'Hello me very good mateys ...', font=font, fill=1)
draw.text((0, 10), 'Well now, what would you like', font=font, fill=1)
draw.text((0, 20), 'to be told this sunny Sunday?', font=font, fill=1)
draw.text((0, 30), 'Would a wild story amuse you?', font=font, fill=1)
draw.text((0, 40), 'This is a very long statement,', font=font, fill=1)
draw.text((0, 50), 'so believe it if you like.', font=font, fill=1)
oled.display()


sleep(3)
draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=20, fill=0)
font = ImageFont.truetype('FreeSans.ttf', 14)
draw.text((0, 0), 'Hello me good mateys', font=font, fill=1)
draw.text((0, 15), 'What would you like', font=font, fill=1)
draw.text((0, 30), 'to be told this day?', font=font, fill=1)
draw.text((0, 45), 'This is a long story,', font=font, fill=1)
oled.display()

sleep(3)
oled.onoff(0)   # kill the oled.  RAM contents still there.
sleep(3)
oled.onoff(1)   # Wake it up again. Display contents intact

sleep(3)
oled.cls()      # Oled still on, but screen contents now blacked out
